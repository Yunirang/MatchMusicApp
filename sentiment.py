from resources.helper_words import custom_words
from get_songs import get_recommended_songs, save_playlist
from mood_mapper import get_contextual_mood


import json 
from datetime import datetime
from nrclex import NRCLex

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# logger for sentinment tracking 

def log_session(user_input, sentiment_data):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "input": user_input,
        "mood": sentiment_data.get('mood') or sentiment_data.get('vader_mood'),
        "vader_scores": sentiment_data.get('polarity_scores') or sentiment_data.get('vader_scores'),
        "emotions": sentiment_data.get('emotions') or sentiment_data.get('nrc_emotions')
    }

    with open("run_log.ndjson", "a") as log_file:
        log_file.write(json.dumps(entry) + "\n")

# gets responses for exporting to txt and to UI 

def get_response(user_input, genre='', prefer_playlist=False, prefer_top_artists=False):
    sentiment = analyze_sentiment(user_input)

    mood_data = {
        "vader_mood": sentiment['mood'],
        "vader_scores": sentiment['polarity_scores'],
        "nrc_emotions": sentiment['emotions'],
        "genre": genre,
        "prefer_playlist": prefer_playlist,
        "prefer_top_artists": prefer_top_artists  # <-- Add this line
    }

    print("INSIDE get_response, prefer_top_artists passed:", prefer_top_artists)


    songs = get_recommended_songs(mood_data, 60)
    playlist_path = save_playlist(sentiment['mood'], songs)

    log_session(user_input, sentiment)

    return {
        "input": user_input,
        "mood": sentiment['mood'],
        "songs": songs,
        "playlist_path": playlist_path
    }



# You only need to download this once
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Update the VADER lexicon with custom words
sia = SentimentIntensityAnalyzer()
sia.lexicon.update(custom_words)


    
# gets emotions from nrclex
def get_emotion_label(text): 
    emotion_obj = NRCLex(text)
    emotions = emotion_obj.top_emotions
    return emotions

# compiles sentiment 
def analyze_sentiment(text):

    polarity_scores = sia.polarity_scores(text)
    # mood_score = get_mood_label(polarity_scores) # not using due to using contextual_model
    emotion_scores = get_emotion_label(text)

    # Get contextual mood
    contextual_mood = get_contextual_mood(text, polarity_scores, emotion_scores)

    # Combine the scores into a single dictionary
    combined_scores = {
        'mood': contextual_mood,
        'polarity_scores': polarity_scores,
        'emotions': emotion_scores
    }

    return combined_scores


