from resources.helper_words import contextual_mood_keywords

# for mapping context based moods 

def get_contextual_mood(text, vader_score, nrc_emotions):
    text = text.lower()
    compound = vader_score.get("compound", 0)

   # Keyword-based override using external mapping
    for mood, triggers in contextual_mood_keywords.items():
        if any(phrase in text for phrase in triggers["phrases"]):
            return mood
        if any(word in text.split() for word in triggers["words"]):  # strict word match
            return mood

    # Emotion-based override
    top_emotions = [e[0] for e in nrc_emotions]

    if "fear" in top_emotions:
        return "reassurance"

    if "anger" in top_emotions:
        return "cool_down"

    if "joy" in top_emotions and compound > 0.6:
        return "celebrate"

    # Compound-based override
    if compound <= -0.6:
        return "deep_sad"
    elif compound >= 0.6:
        return "uplift"
    elif -0.2 < compound < 0.2:
        return "neutral"
    elif compound < 0:
        return "sad"
    else:
        return "content"
