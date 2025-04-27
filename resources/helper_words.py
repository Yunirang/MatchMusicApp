custom_words = {
    # Strong negative
    "depressed": -3.5,
    "miserable": -3.2,
    "devastated": -3.0,
    "overwhelmed": -2.5,
    "burned out": -2.5,
    "exhausted": -2.5,
    "frustrated": -2.2,
    "lonely": -2.1,
    "hopeless": -2.3,
    "angry": -2.4,
    "furious": -3.0,
    "anxious": -2.2,
    "numb": -2.0,
    "worried": -1.9,
    "disappointed": -2.3,
    "guilty": -2.0,
    "ashamed": -2.3,
    "worthless": -2.7,
    "empty": -2.0,
    "crying": -2.8,
    "jealous": -1.8,
    "envious": -1.7,
    "stressed": -2.2,
    "tired": -1.5,
    "drained": -1.8,
    "irritated": -1.6,
    "angsty": -1.5,
    "panicked": -2.2,
    "suffocating": -2.8,
    "heartbroken": -3.0,
    "regret": -2.3,
    "resentful": -2.0,
    "grieving": -2.9,
    "melancholy": -2.0,
    "rage": -3.2,
    "worthless": -2.8,
    "broken": -2.7,
    "confused": -1.4,
    "isolated": -2.3,
    "lost": -1.9,
    "trapped": -2.2,
    "rejected": -2.5,
    "discouraged": -2.1,
    "apathetic": -2.0,
    "hopelessness": -2.6,
    "overworked": -2.0,
    "underappreciated": -1.8,

    # Strong positive
    "happy": 2.5,
    "joyful": 2.8,
    "grateful": 2.4,
    "energized": 2.6,
    "confident": 2.3,
    "relaxed": 2.1,
    "calm": 2.0,
    "peaceful": 2.2,
    "excited": 2.6,
    "hopeful": 2.4,
    "content": 2.2,
    "inspired": 2.5,
    "empowered": 2.3,
    "refreshed": 2.1,
    "motivated": 2.3,
    "uplifted": 2.4,
    "loved": 2.6,
    "blessed": 2.7,
    "focused": 2.0,
    "determined": 2.1,
    "cheerful": 2.5,
    "amused": 2.3,
    "proud": 2.2,
    "playful": 2.0,
    "creative": 2.1,
    "free": 2.0,
    "supportive": 2.2,
    "productive": 2.1,
    "fulfilled": 2.4,
    "satisfied": 2.2,
    "thrilled": 2.7,
    "positive": 2.0,
    "giddy": 2.3,
    "secure": 2.1,
    "joyous": 2.7,
    "balanced": 2.0,
    "safe": 2.0,
    "optimistic": 2.4,
    "rejuvenated": 2.2,
    "strong": 2.0,
    "glad": 2.3,
    "loving": 2.5,
    "peace": 2.3,
    "sunny": 2.0,
    "thankful": 2.2,
    "hope": 2.0,
    "laughing": 2.3,
    "relieved": 2.1, 
    "anhedonia": -3.0,
    "worthlessness": -2.9,
    "despair": -3.2,
    "insecure": -1.9,
    "burnout": -2.6,
    "bleak": -2.8,
    "hopelessly": -2.9,
    "invisible": -2.1,
    "misunderstood": -2.0,
    "unloved": -2.6,
    "torn": -2.3,
    "dread": -2.7,
    "pointless": -2.8,
    "hollow": -2.3,
    "useless": -2.7,
    "fatigued": -2.0,
    "crybaby": -1.5,
    "shattered": -2.8,
    "zen": 2.3,
    "peacefully": 2.2,
    "vibrant": 2.4,
    "elated": 2.7,
    "ecstatic": 2.8,
    "serene": 2.3,
    "euphoric": 2.9,
    "radiant": 2.5,
    "bubbly": 2.2,
    "sparkling": 2.1,
    "grinning": 2.3,
    "cheering": 2.4,
    "smiling": 2.2,
    "winning": 2.0,
    "high-spirited": 2.3,
    "glowing": 2.3,
    "beaming": 2.5,
    "joyfully": 2.6,
    "comforted": 2.2,
    "contentedly": 2.1
}



# resources/helper_words.py

contextual_mood_keywords = {
    "sleepy": {
        "phrases": [
            "i want to sleep", "need to sleep", "go to bed", "fall asleep", "trying to sleep",
            "can’t keep my eyes open", "bedtime", "sleepy vibes", "i feel sleepy", "i'm going to sleep",
            "i should sleep", "dozing off", "past my bedtime", "falling asleep at my desk",
            "barely awake", "about to knock out", "nap sounds good", "so ready for bed",
            "curl up and sleep", "mind shutting down"
        ],
        "words": [
            "sleepy", "drowsy", "yawning", "slumber", "groggy", "fatigued", "lazy", "napping",
            "snooze", "tired", "drained", "exhausted", "weary", "slow", "foggy", "worn out",
            "dozy", "dreamy", "zzz", "lethargic", "sluggish", "burnt out", "sapped", "listless",
            "faint", "restless", "melatonin", "nod", "pillow", "lights out"
        ]
    },
    "energize": {
        "phrases": [
            "time to move", "morning run", "get the blood flowing", "hyped for today",
            "ready to hustle", "feeling the burn", "wake up strong", "adrenaline rush",
            "morning energy", "let’s get started", "bounce back", "power through",
            "move and groove", "pep in my step", "rise and shine", "kick into gear",
            "starting strong", "feeling charged", "just finished coffee", "up and moving"
        ],
        "words": [
            "energized", "awake", "pumped", "motivated", "strong", "vital", "brisk", "bouncy",
            "focused", "electric", "wired", "active", "zest", "lively", "driven", "ready",
            "strong-willed", "amped", "uplifted", "revved", "agile", "surge", "vigorous",
            "powerful", "refresh", "vibrant", "kicking", "rejuvenated", "unstoppable", "invigorated"
        ]
    },
    "focus": {
        "phrases": [
            "time to study", "need to focus", "entering deep work", "distraction-free",
            "mental clarity", "get into the zone", "ready to concentrate", "blocking everything out",
            "need to zone in", "grind mode", "deadline coming", "focus time", "time to lock in",
            "brainpower mode", "tunnel vision activated", "laser sharp", "mental drive",
            "intense work session", "executive function", "zero distractions"
        ],
        "words": [
            "focus", "studying", "concentration", "clarity", "locked", "task", "grind", "work",
            "immersed", "productive", "study", "goal", "commit", "tuned", "efficient", "discipline",
            "sharp", "intent", "fixated", "engaged", "tunnel", "precise", "organized", "alert",
            "cognitive", "reading", "strategic", "absorbed", "goal-setting", "diligent"
        ]
    },
    "breakup": {
        "phrases": [
            "got dumped", "broken heart", "relationship ended", "just broke up",
            "mourning love", "love is gone", "i miss them", "we’re not together",
            "still love them", "they left me", "i’m alone now", "can’t move on",
            "heart is aching", "wish they stayed", "it's over now", "hurts to breathe",
            "can’t stop crying", "love lost", "goodbye forever", "emotional wreck"
        ],
        "words": [
            "breakup", "heartbroken", "lost love", "separation", "grief", "sadness", "abandoned",
            "loneliness", "missing", "regret", "tears", "crying", "remorse", "pain", "sorrow",
            "isolation", "bitter", "wistful", "guilt", "ache", "emptiness", "resentment",
            "longing", "yearning", "anguish", "nostalgia", "unloved", "forsaken", "distraught", "tormented"
        ]
    },
    "recharge": {
        "phrases": [
            "too much work", "mentally exhausted", "need a break", "worn down", "can't focus",
            "overwhelmed with stress", "losing steam", "stretched too thin", "too many tasks",
            "feeling burnout", "need recovery", "emotionally drained", "my mind is fried",
            "mental overload", "zero capacity", "done for the day", "need rest time",
            "not thinking straight", "everything’s too much", "overstimulated"
        ],
        "words": [
            "burned out", "overworked", "overwhelmed", "exhausted", "stressed", "fatigued", "anxious",
            "worn", "slow", "shaky", "tense", "fragile", "unfocused", "rattled", "frazzled",
            "cluttered", "maxed", "numb", "tired", "depleted", "uninspired", "foggy", "jittery",
            "restless", "impatient", "moody", "edgy", "snappy", "strained", "fogged"
        ]
    },
    "wind_down": {
        "phrases": [
            "need to relax", "time to chill", "calm down", "peace and quiet", "end of day vibes",
            "winding down", "slow evening", "relaxation mode", "getting cozy", "evening tea",
            "taking it easy", "decompress time", "cooling off", "let go of stress", "breathe easy",
            "gentle mood", "cozy atmosphere", "peaceful environment", "settling down", "time to breathe"
        ],
        "words": [
            "relax", "chill", "calm", "peaceful", "unwind", "decompress", "soothing", "gentle",
            "serene", "zen", "mellow", "ease", "tranquil", "slow", "still", "quiet", "harmonious",
            "meditative", "light", "floating", "silent", "cozy", "dim", "retreat", "graceful",
            "subtle", "restful", "soft", "laid-back", "easeful"
        ]
    },
    "hype": {
        "phrases": [
            "game time", "let's go", "get lit", "turn up", "bring it on", "go time", "i'm pumped",
            "can’t wait", "full energy", "high power", "ready to go", "all in", "dominate the day",
            "race mode", "battle ready", "unstoppable force", "feel the power", "beast mode",
            "peak performance", "next level hype"
        ],
        "words": [
            "hype", "pump", "ready", "amped", "fired up", "motivated", "loud", "energized",
            "thrilled", "excited", "intense", "powerful", "furious", "raging", "fast", "rush",
            "burst", "maxed", "alive", "explode", "hyper", "banger", "party", "blasting", "ecstatic",
            "adrenaline", "raw", "crazy", "cranked", "wired"
        ]
    }
}


TOP_ARTISTS_BY_GENRE = {
    'pop': [
        'Taylor Swift', 'Dua Lipa', 'Harry Styles', 'Ariana Grande', 'Olivia Rodrigo',
        'Ed Sheeran', 'Justin Bieber', 'Katy Perry', 'Shawn Mendes'
    ],
    'rock': [
        'Foo Fighters', 'Muse', 'The Killers', 'Red Hot Chili Peppers', 'Nirvana',
        'Green Day', 'Arctic Monkeys', 'Linkin Park', 'Imagine Dragons'
    ],
    'hip hop': [
        'Drake', 'Kendrick Lamar', 'J. Cole', 'Travis Scott', 'Nicki Minaj',
        'Kanye West', 'Lil Baby', 'Post Malone', '21 Savage'
    ],
    'lofi': [
        'Idealism', 'Nymano', 'Jinsang', 'L’indécis', 'Kupla',
        'EEVEE', 'fantompower', 'Leavv', 'Saib'
    ],
    'jazz': [
        'Miles Davis', 'John Coltrane', 'Ella Fitzgerald', 'Louis Armstrong', 'Thelonious Monk',
        'Duke Ellington', 'Chet Baker', 'Bill Evans', 'Charlie Parker'
    ],
    'edm': [
        'Calvin Harris', 'David Guetta', 'Zedd', 'Marshmello', 'Avicii',
        'Martin Garrix', 'Kygo', 'Alan Walker', 'Deadmau5'
    ],
    'classical': [
        'Yo-Yo Ma', 'Lang Lang', 'Anne-Sophie Mutter', 'Itzhak Perlman', 'Martha Argerich',
        'Hilary Hahn', 'Vladimir Horowitz', 'Daniel Barenboim', 'Jacqueline du Pré'
    ],
    'country': [
        'Luke Bryan', 'Carrie Underwood', 'Chris Stapleton', 'Miranda Lambert', 'Blake Shelton',
        'Kacey Musgraves', 'Morgan Wallen', 'Keith Urban', 'Tim McGraw'
    ],
    'indie': [
        'Arctic Monkeys', 'Tame Impala', 'Phoebe Bridgers', 'Mac DeMarco', 'Bon Iver',
        'Vampire Weekend', 'The 1975', 'Florence and the Machine', 'Mitski'
    ],
    'r&b': [
        'SZA', 'The Weeknd', 'HER', 'Frank Ocean', 'Giveon',
        'Alicia Keys', 'Daniel Caesar', 'Jhené Aiko', 'Brent Faiyaz'
    ],
    'metal': [
        'Metallica', 'Slipknot', 'Avenged Sevenfold', 'Iron Maiden', 'System of a Down',
        'Megadeth', 'Pantera', 'Tool', 'Lamb of God'
    ],
    'blues': [
        'B.B. King', 'Eric Clapton', 'Muddy Waters', 'Stevie Ray Vaughan', 'John Lee Hooker',
        'Buddy Guy', 'Robert Johnson', 'Etta James', 'Howlin’ Wolf'
    ],
    'folk': [
        'Bob Dylan', 'Fleet Foxes', 'Iron & Wine', 'Mumford & Sons', 'Simon & Garfunkel',
        'The Lumineers', 'Of Monsters and Men', 'Nick Drake', 'Sufjan Stevens'
    ],
    'ambient': [
        'Brian Eno', 'Aphex Twin', 'Moby', 'Tycho', 'Boards of Canada',
        'Helios', 'Loscil', 'Carbon Based Lifeforms', 'Hammock'
    ]
}



