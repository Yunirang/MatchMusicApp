MelodyMatch: An Emotion-Aware Music Recommender

MelodyMatch is a lightweight local web application that analyzes your emotions based on text input and recommends music accordingly.  
It supports both **individual song suggestions** and **full playlist generation**, with **genre filtering**, **top artist boosting**, and **animated mood reactions**.

Built with Python (Flask), NLTK, NRC Emotion Lexicon, and YouTube search.

How to Run the App

1. Clone the repository or open the project locally:

```bash
git clone <your-repo-url>
cd MelodyMatch
```

2. Set up a virtual environment:

For Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
For Windows:

```bash
venv\Scripts\activate
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

5. Open your browser and go to:

```
http://127.0.0.1:5000
```

How to Use

1. Type how you're feeling in the input box (or use voice input!).
2. Optionally select a music genre.
3. Choose between getting individual songs or full playlists.
4. (Optional) Boost results using top artists for your selected genre.
5. Submit, and get music that matches your emotional tone!
6. Download your personalized playlist as a `.txt` file.
7. Toggle between dark and light mode using the switch.

> Animated emoji reactions appear based on your detected mood.  
> Loading tips guide you while your songs are being prepared.

Project File Structure

```
MelodyMatch/
├── app.py                    # Flask app runner
├── sentiment.py               # Handles sentiment and mood analysis
├── get_songs.py               # YouTube API-based song recommendation and playlist saving
├── mood_mapper.py             # Custom context-aware mood logic
├── run_log.ndjson             # Logs user interactions (optional, can .gitignore)
│
├── resources/
│   ├── helper_words.py        # Custom sentiment word weights + top artists by genre
│   ├── offline_fallback.py    # Offline fallback songs for each mood
│
├── generated_playlists/       # Exported playlists (.txt files)
│
├── static/
│   ├── style.css              # Styling for landing, loading, dark mode, mood animations
│   └── script.js              # Frontend logic, AJAX, emoji animation, loading tips
│
├── templates/
│   └── index.html             # Main frontend HTML (Flask + Jinja2)
│
├── venv/                      # Local virtual environment (excluded from Git)
└── README.md                  # This file
```

Key Features

- **Advanced Sentiment Analysis:** Combines VADER polarity, NRC emotions, and custom contextual keyword mapping.
- **Context-aware Mood Detection:** Understands deeper nuances (e.g., "I want to sleep" ≠ "I'm tired").
- **Dynamic YouTube Music Retrieval:** Fetches songs and playlists based on mood, genre, and artist boosting.
- **Offline Fallbacks:** If online search fails, fallback playlists are provided automatically.
- **Mood-Based Emoji Animations:** Floating emojis based on your detected feeling (sleepy, hype, sad, etc.).
- **Friendly UX:** Random loading tips, mood suggestions, clean transitions.
- **Light and Dark Mode Toggle:** Easy switching between themes.
- **Fully Local:** No cloud hosting required — runs on your machine via Flask.

Potential Future Improvements

- Integrate Spotify or Apple Music APIs for more structured results
- Add direct "play preview" buttons without needing external links
- Implement more nuanced query rewriting for YouTube
- Add mobile responsiveness for full cross-device experience

Built With

- Python (Flask)
- NLTK (VADER Sentiment Analyzer)
- NRC Emotion Lexicon
- YouTube-Search-Python
- HTML / CSS / JavaScript (Vanilla)
- Love for music 
