import streamlit as st
import random

def fun_zone():
    # --- CSS Styling for a Fun, Relaxing Look ---
    st.markdown("""
        <style>
        body {
            background-color: #f0fbfc;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            background: linear-gradient(to right, #00bfa5, #0288d1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-top: 20px;
        }
        .section-title {
            font-size: 24px;
            color: #004d66;
            margin-top: 30px;
        }
        .fade-in {
            animation: fadeIn 2s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .recommend-box {
            background-color: #ffffff;
            border-left: 6px solid #00bfa5;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        .motivation-box {
            background: linear-gradient(135deg, #a7ffeb, #e0f7fa);
            padding: 16px;
            border-radius: 12px;
            text-align: center;
            font-size: 18px;
            color: #006064;
            margin-top: 25px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        button {
            transition: 0.3s ease-in-out;
        }
        button:hover {
            transform: scale(1.05);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Title ---
    st.markdown("<div class='title fade-in'>🌈 Mood Booster Zone</div>", unsafe_allow_html=True)
    st.markdown("<p class='fade-in' style='text-align:center; color:#007c91;'>A little laughter, music, and fun to brighten your day!</p>", unsafe_allow_html=True)

    # --- Comedy Movie Suggestions ---
    st.markdown("<div class='section-title'>🎬 Comedy Movies</div>", unsafe_allow_html=True)
    movies = [
        "Paddington (2014)", "Despicable Me", "Sing", "The Lego Movie", "The Boss Baby",
        "Home Alone", "The Peanuts Movie", "Mr. Bean's Holiday", "Finding Dory", "Minions"
    ]
    for movie in movies:
        st.markdown(f"<div class='recommend-box'>🍿 {movie}</div>", unsafe_allow_html=True)

    # --- Relaxing Songs ---
    st.markdown("<div class='section-title'>🎵 Relaxing Songs / Playlists</div>", unsafe_allow_html=True)
    playlists = {
        "Lo-fi Chill Mix": "https://www.youtube.com/watch?v=jfKfPfyJRdk",
        "Relaxing Nature Sounds 🌳": "https://www.youtube.com/watch?v=eKFTSSKCzWA",
        "Upbeat Happy Vibes": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "Instrumental Focus Playlist": "https://www.youtube.com/watch?v=5qap5aO4i9A"
    }
    for name, url in playlists.items():
        st.markdown(f"<div class='recommend-box'>🎧 <a href='{url}' target='_blank'>{name}</a></div>", unsafe_allow_html=True)

    # --- Fun Activities ---
    st.markdown("<div class='section-title'>🧩 Fun Activities</div>", unsafe_allow_html=True)
    activities = [
        "🖌️ Try Online Coloring Books: [Happy Color](https://play.google.com/store/apps/details?id=com.pixel.art.coloring.color.number&hl=en&gl=US)",
        "💃 Follow a Dance Workout: [Just Dance Kids](https://www.youtube.com/watch?v=ziLHZeKbMUo)",
        "🌬️ Practice Deep Breathing: [Box Breathing](https://www.youtube.com/watch?v=tEmt1Znux58)",
        "📖 Read a Silly Story: [Storyberries](https://www.storyberries.com/funny-stories-for-kids/)",
        "🧠 Try Memory Card Games: [Online Game](https://www.memozor.com/memory-games/for-kids/animals)"
    ]
    for act in activities:
        st.markdown(f"<div class='recommend-box'>{act}</div>", unsafe_allow_html=True)

    # --- Motivational Quote Generator ---
    st.markdown("<div class='section-title'>💡 Motivational Quote</div>", unsafe_allow_html=True)
    quotes = [
        "You are braver than you believe, stronger than you seem, and smarter than you think.",
        "Every day may not be good, but there's something good in every day.",
        "Mistakes are proof you are trying!",
        "Your only limit is your mind. Keep pushing forward!",
        "Small steps every day make big results over time.",
        "It's okay to rest. Just don’t quit."
    ]
    quote = random.choice(quotes)
    st.markdown(f"<div class='motivation-box fade-in'>🌟 {quote}</div>", unsafe_allow_html=True)

    # --- Go Back to Home Prediction Page ---
    if st.button("🔮 Go to ADHD Prediction Page"):
        st.experimental_set_query_params()  # clears current page
        st.rerun()
