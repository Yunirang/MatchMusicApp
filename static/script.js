document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.getElementById('toggle-theme');
    const splash = document.getElementById('landing-screen');
    const mainContainer = document.querySelector('.container');
    const form = document.querySelector('form');
    const loading = document.getElementById('loading-screen');
    const resultContainer = document.getElementById('results');
    const moodTitle = document.getElementById('mood-title');
    const songList = document.getElementById('song-list');
    const downloadLink = document.getElementById('download-link');
    const leftAnim = document.getElementById('mood-animation-left');
    const rightAnim = document.getElementById('mood-animation-right');

    const loadingTipText = document.getElementById('loading-tip'); // NEW: loading tip placeholder

    const voiceButton = document.getElementById('start-voice');
    const feelingInput = document.getElementById('feeling');

    // NEW: Array of loading tips
    const loadingTips = [
        "Tip: Try moods like 'hype' or 'focus'!",
        "Tip: You can search by feeling or genre.",
        "Tip: Prefer playlists? Check the box!",
        "Tip: Uplift your mood with happy songs!",
        "Tip: Deep sad brings emotional ballads.",
        "Tip: Focus mode is great for studying!",
        "Tip: Recharge with calming music.",
        "Tip: Try 'celebrate' for party playlists!",
        "Tip: 'Sleepy' gives you soft lullabies.",
        "Tip: Music changes your mood. Explore!"
    ];

    let splashAlreadyHidden = false;

    if (voiceButton && feelingInput && 'webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.lang = 'en-US';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        voiceButton.addEventListener('click', () => {
            recognition.start();
            voiceButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        });

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            feelingInput.value = transcript;
            voiceButton.innerHTML = '<i class="fas fa-microphone"></i>';
        };

        recognition.onerror = () => {
            voiceButton.innerHTML = '<i class="fas fa-microphone"></i>';
        };

        recognition.onend = () => {
            voiceButton.innerHTML = '<i class="fas fa-microphone"></i>';
        };
    }

    // Toggle light/dark mode
    if (toggle) {
        toggle.addEventListener('click', function () {
            document.body.classList.toggle('dark-mode');
        });
    }

    // Hide splash screen
    function hideSplash() {
        if (splash && !splashAlreadyHidden) {
            splash.classList.add('fade-out');
            setTimeout(() => {
                splash.style.display = 'none';
                mainContainer.style.opacity = 1;
                splashAlreadyHidden = true;
            }, 1000);
        }
    }

    if (splash) {
        setTimeout(hideSplash, 2500);
        splash.addEventListener('click', hideSplash);
    }

    // Form submission (AJAX)
    if (form && loading) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            hideSplash();
            loading.classList.add('show');

            // NEW: Pick random tip when loading starts
            if (loadingTipText) {
                const randomTip = loadingTips[Math.floor(Math.random() * loadingTips.length)];
                loadingTipText.textContent = randomTip;
            }

            const feeling = form.feeling.value;
            const genre = form.genre.value;
            const preferPlaylist = form.preferPlaylist.checked;
            const preferTopArtists = form.preferTopArtists.checked;

            fetch('/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ feeling, genre, preferPlaylist, preferTopArtists })
            })
            .then(response => response.json())
            .then(data => {
                setTimeout(() => {
                    loading.classList.remove('show');
                    if (loadingTipText) loadingTipText.textContent = ""; // NEW: Clear loading tip
                    displayResults(data);
                    triggerMoodAnimation(data.mood);
                }, 600);
            })
            .catch(error => {
                console.error('Error:', error);
                loading.classList.remove('show');
                if (loadingTipText) loadingTipText.textContent = ""; // NEW: Clear loading tip
            });
        });
    }
        
    // Clean title function (improved)
    function cleanTitle(rawTitle) {
        if (!rawTitle) return '';

        // Remove emojis and non-standard characters
        const asciiTitle = rawTitle.replace(/[^\x00-\x7F]/g, '');

        // Remove brackets/parentheses content like [Official Video] or (Lyrics)
        let cleaned = asciiTitle
            .replace(/\\[[^\\]]*\\]|\\([^\\)]*\\)/g, '')  // remove [text] and (text)
            .replace(/\\b(official|audio|video|lyrics|HD|remastered|remaster|cover)\\b/gi, '') // remove common noise words
            .replace(/\\s+/g, ' ')  // collapse extra spaces
            .trim();

        // Safety fallback: if cleaned title is too short, use original asciiTitle
        if (cleaned.length < 5) {
            cleaned = asciiTitle.trim();
        }

        // Shorten very long titles
        if (cleaned.length > 90) {
            cleaned = cleaned.substring(0, 87) + '...';
        }

        return cleaned;
    }

    
    // Show results
    function displayResults(data) {
        if (moodTitle) {
            const formattedMood = data.mood
                .replace(/_/g, ' ')
                .replace(/\b\w/g, c => c.toUpperCase());
            moodTitle.innerHTML = `<i class="fas fa-music"></i> Detected Mood: ${formattedMood}`;
        }

        if (songList) {
            songList.innerHTML = '';
            if (data.songs.length === 0 || (data.songs.length === 1 && data.songs[0].includes('No songs found'))) {
                const li = document.createElement('li');
                li.innerHTML = "<p style='font-style: italic; color: #999;'>😕 Sorry, we couldn't find any songs for that mood. Try another feeling or genre!</p>";
                songList.appendChild(li);
            } else {
                data.songs.forEach(song => {
                    const li = document.createElement('li');
                    li.classList.add('song-card');
            
                    const parts = song.split(' - ');
                    const title = cleanTitle(parts[0]);
                    const url = parts[1] && parts[1].startsWith('http') ? parts[1] : null;
                    if (!url) return;
            
                    const embedUrl = embedYouTube(url);
                    li.innerHTML = `
                        <p><a href="${url}" target="_blank" rel="noopener noreferrer">${title}</a></p>
                        ${embedUrl ? `
                            <iframe width="100%" height="150" src="${embedUrl}" frameborder="0" allowfullscreen></iframe>
                        ` : '<p style="color: #999; font-style: italic;">Preview unavailable</p>'}
                    `;
                    songList.appendChild(li);
                });
            }            
        }

        if (downloadLink && data.playlist_path) {
            downloadLink.href = data.playlist_path;
            downloadLink.style.display = 'block';
        }

        if (resultContainer) {
            resultContainer.style.display = 'block';
            resultContainer.scrollIntoView({ behavior: 'smooth' });
        }
    }

    // Convert YouTube URL to embeddable format
    function embedYouTube(url) {
        try {
            let videoId = '';
            if (url.includes('watch?v=')) {
                videoId = new URL(url).searchParams.get('v');
            } else if (url.includes('youtu.be/')) {
                videoId = url.split('youtu.be/')[1].split('?')[0];
            }
            if (!videoId || videoId.length < 6) return null;
            return `https://www.youtube.com/embed/${videoId}`;
        } catch (e) {
            return null;
        }
    }

    // Floating mood-based emoji animation
    function triggerMoodAnimation(mood) {
        if (!leftAnim || !rightAnim) return;

        leftAnim.innerHTML = '';
        rightAnim.innerHTML = '';

        let emojis = [];

        switch (mood) {
            case 'sleepy':
                emojis = ['🛌', '😴', '🌙', '💤'];
                break;
            case 'energize':
                emojis = ['⚡', '💪', '🏃‍♂️', '🔥'];
                break;
            case 'focus':
                emojis = ['🧠', '📚', '💡', '👓'];
                break;
            case 'breakup':
                emojis = ['💔', '😭', '🍫', '📺'];
                break;
            case 'recharge':
                emojis = ['🧘‍♀️', '🛀', '🌿', '☕'];
                break;
            case 'wind_down':
                emojis = ['🛌', '🌙', '🕯️', '🎧'];
                break;
            case 'hype':
                emojis = ['🔥', '🎤', '🏆', '🕺'];
                break;
            case 'reassurance':
                emojis = ['🫂', '💖', '🌈', '🤝'];
                break;
            case 'cool_down':
                emojis = ['💨', '😌', '🧊', '🍃'];
                break;
            case 'celebrate':
                emojis = ['🎉', '🎊', '✨', '🥳'];
                break;
            case 'deep_sad':
                emojis = ['🌧️', '😔', '💧', '💤'];
                break;
            case 'uplift':
                emojis = ['🌞', '🎶', '💫', '🌼'];
                break;
            case 'sad':
                emojis = ['💖', '🫂', '✨', '🍀'];
                break;
            case 'neutral':
                emojis = ['🌫️', '🔄', '🌥️'];
                break;
            case 'content':
                emojis = ['😊', '🍃', '☀️', '🎵'];
                break;
            default:
                emojis = ['🎶'];
        }

        for (let i = 0; i < 12; i++) {
            const e = document.createElement('span');
            e.className = 'emoji-bubble';
            e.textContent = emojis[Math.floor(Math.random() * emojis.length)];
            e.style.left = `${Math.random() * 80}px`;
            e.style.top = `${Math.random() * 300}px`;
            e.style.animationDelay = `${Math.random() * 2}s`; // adjusting the trigger delay 
            (Math.random() > 0.5 ? leftAnim : rightAnim).appendChild(e);
        }
    }
});
