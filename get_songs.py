from youtubesearchpython import VideosSearch
from resources.offline_fallback import fallback_songs
from resources.helper_words import TOP_ARTISTS_BY_GENRE
from resources.mood_synonyms import MOOD_SYNONYMS

import os
import random



def build_search_query(mood, genre, prefer_playlist, prefer_top_artists):
    mood_part = mood.replace("_", " ").strip()
    genre_part = genre.strip() if genre else ""

    # Expand mood using synonyms
    expanded_mood = mood_part
    if mood.lower() in MOOD_SYNONYMS:
        synonyms = MOOD_SYNONYMS[mood.lower()]
        selected_synonym = random.choice(synonyms)
        expanded_mood += f" {selected_synonym}"

    base_query = f"{expanded_mood} {genre_part} songs".strip()

    # Add top artists naturally
    if prefer_top_artists and genre and genre.lower() in TOP_ARTISTS_BY_GENRE:
        artists_list = TOP_ARTISTS_BY_GENRE[genre.lower()]
        selected_artist = random.choice(artists_list)
        base_query += f" {selected_artist}"

    # Add playlist preference naturally
    if prefer_playlist:
        base_query += " playlist"

    print(f"SEARCH QUERY: {base_query}")

    return base_query



def get_youtube_links(query, max_results, prefer_playlist=False):
    try:
        videos_search = VideosSearch(query, limit=200)
        results = videos_search.result()
    except Exception as e:
        print("YouTube API error:", e)
        return []

    all_links = []

    for video in results['result']:
        title = video.get('title', '').lower()
        link = video.get('link', '')

        # If user wanted playlists, prioritize titles that mention playlists/mixes
        if prefer_playlist:
            if not any(kw in title for kw in ['playlist', 'mix', 'hour', 'nonstop']):
                continue

        all_links.append(f"{video['title']} - {link}")

    all_links = list(dict.fromkeys(all_links))  # remove duplicates
    random.shuffle(all_links)

    return all_links[:max_results] if all_links else None


def get_recommended_songs(mood_data, max_results):
    """
    Get songs based on user mood and preferences.
    """
    genre = mood_data.get("genre", "")
    prefer_playlist = mood_data.get("prefer_playlist", False)
    prefer_top_artists = mood_data.get("prefer_top_artists", False)
    vader_mood = mood_data.get("vader_mood") or mood_data.get("mood")

    # 1. Try VADER mood
    if vader_mood:
        try:
            query = build_search_query(vader_mood, genre, prefer_playlist, prefer_top_artists)
            links = get_youtube_links(query, max_results, prefer_playlist=prefer_playlist)
            if links:
                return links
        except Exception:
            pass

    # 2. Try fallback to NRC emotions
    for emotion, _ in mood_data.get("nrc_emotions", []):
        try:
            query = build_search_query(emotion, genre, prefer_playlist, prefer_top_artists)
            links = get_youtube_links(query, max_results, prefer_playlist=prefer_playlist)
            if links:
                return links
        except Exception:
            continue

    # 3. Offline fallback
    if vader_mood and vader_mood in fallback_songs:
        songs = fallback_songs[vader_mood]
        random.shuffle(songs)
        return songs[:max_results] if songs else None

    return ["No songs found for the given mood."]


def save_playlist(mood, songs, filename=None):
    os.makedirs('generated_playlists', exist_ok=True)

    if not filename:
        filename = f"{mood}_pl.txt"

    full_path = os.path.join('generated_playlists', filename)

    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(f"Playlist for {mood} mood:\n")
        for idx, song in enumerate(songs, start=1):
            file.write(f"{idx}. {song}\n")

    return os.path.abspath(full_path)
