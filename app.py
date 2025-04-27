from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from sentiment import get_response

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Needed for session management

# Home route with GET/POST for traditional form flow
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['feeling']
        result = get_response(user_input)

        # Store results temporarily in session
        session['input'] = user_input
        session['mood'] = result['mood']
        session['songs'] = result['songs']
        session['playlist_path'] = result['playlist_path']

        # Redirect to the same page via GET (Post-Redirect-Get pattern)
        return redirect(url_for('index'))

    # On GET: check if data exists in session
    user_input = session.pop('input', None)
    mood = session.pop('mood', None)
    songs = session.pop('songs', None)
    playlist_path = session.pop('playlist_path', None)

    return render_template(
        'index.html',
        show_landing=user_input is None,  # show splash only on clean load
        input=user_input,
        mood=mood,
        songs=songs,
        playlist_path=playlist_path
    )

# NEW: AJAX route for fetch requests
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    user_input = data.get('feeling', '')
    genre = data.get('genre', '').strip().lower()
    prefer_playlist = data.get('preferPlaylist', False)
    prefer_top_artists = data.get('preferTopArtists', False)

    print("ANALYZE RECEIVED prefer_top_artists:", prefer_top_artists)


    result = get_response(user_input, genre, prefer_playlist, prefer_top_artists)

    return jsonify({
        'mood': result['mood'],
        'songs': result['songs'],
        'playlist_path': result['playlist_path']
    })


if __name__ == '__main__':
    app.run(debug=True)
