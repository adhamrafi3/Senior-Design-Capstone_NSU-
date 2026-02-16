import streamlit as st
import streamlit.components.v1 as components
from prediction_helper import predict
import adhd_info
from fun_zone import fun_zone
from coloring_canvas import coloring_canvas  # <-- NEW PAGE IMPORTED
import random

# --- Custom CSS: Animations, styling ---
st.markdown("""
    <style>
    body {
        background-color: #e6f2f3;
    }
    .stApp {
        background-color: #e6f2f3;
        font-family: 'Segoe UI', sans-serif;
        color: #003d4d;
        animation: fadeIn 1.5s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    h1, h2, h3, h4 {
        color: #003d4d;
    }

    .title-effect {
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(to right, #007d8a, #00bfa5, #007d8a);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 4s linear infinite;
        text-align: center;
        font-family: "Trebuchet MS", sans-serif;
    }

    @keyframes shimmer {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    .predict-bounce {
        animation: bounce 1.4s infinite alternate;
    }

    @keyframes bounce {
        from { transform: translateY(0); }
        to { transform: translateY(-8px); }
    }

    .stButton>button {
        background-color: #007d8a;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
        border: none;
        font-weight: bold;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #005f66;
        transform: scale(1.05);
    }

    .css-1cpxqw2, .css-1d391kg, .css-1v0mbdj {
        background-color: #ffffff !important;
        color: #003d4d !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", [
    "ADHD Prediction",
    "About ADHD",
    "Mood Booster Zone",
    "Chill Zone (Snake Game)",
    "Coloring Canvas 🎨"  # <-- NEW PAGE LINK
])

# --- ADHD Prediction Page ---
if page == "ADHD Prediction":
    st.markdown("<div class='title-effect'>ADHD Predictions and Analysis at Early Age</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #004d66;'>Please enter the details below to predict ADHD:</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age in Years", min_value=2, max_value=100, step=1)
        if age < 2 or age > 17:
            st.warning("Please enter an age between 2 and 17 years.")
        input_dict = {
            "SC_AGE_YEARS": age,
            "sex_2122": st.selectbox("Sex of child", ["Male", "Female"]),
            "allergies_2122": st.selectbox("Allergies status", ["Does not have condition", "Ever told, does not currently have", "Currently has condition"]),
            "asthma_2122": st.selectbox("Asthma status", ["Does not have condition", "Ever told, does not currently have", "Currently has condition"]),
            "headache_2122": st.selectbox("Headache status", ["Does not have condition", "Ever told, does not currently have", "Currently has condition"]),
            "anxiety_2122": st.selectbox("Anxiety status", ["Does not have condition", "Ever told, does not currently have", "Currently has condition"]),
            "depress_2122": st.selectbox("Depression status", ["Does not have condition", "Ever told, does not currently have", "Currently has condition"]),
            "behavior_2122": st.selectbox("Behavioral issues status", ["Does not have condition", "Ever told, does not currently have", "Currently has condition"]),
            "GeneticScr_2122": st.selectbox("Genetic screening status", ["Never had condition", "Ever told, not identified by test", "Ever told, identified by test"]),
            "BrainInjTold_2122": st.selectbox("Brain injury status", ["Never thought child has injury", "Ever thought, not confirmed", "Ever had injury confirmed by doctor"])
        }

    with col2:
        input_dict.update({
            "ACE2more6HH_2122": st.selectbox("Household challenges", ["No ACEs", "1 ACE", "2 or more ACEs"]),
            "famstruct5_2122": st.selectbox("Family structure", ["Two parents, married", "Two parents, not married", "Single parent", "Grandparent household", "Other family type"]),
            "fruit_2122": st.selectbox("Fruit consumption", ["Never", "Rarely", "Sometimes", "Regularly", "Often", "Always"]),
            "vegetables_2122": st.selectbox("Vegetable consumption", ["Never", "Rarely", "Sometimes", "Regularly", "Often", "Always"]),
            "Cond2more_2122": st.selectbox("Number of Chronic health conditions", ["None", "One condition", "Multiple conditions"]),
            "CSHCNtype_2122": st.selectbox("Type of special health care needs", ["None", "Functional limitations", "Prescription medication only", "Above-routine use of services", "Medication and above-routine services"]),
            "ChHlthSt_2122": st.selectbox("Child health status", ["Excellent", "Good", "Fair or Poor"]),
            "ExBrstFd_2122": st.selectbox("Exclusive breastfeeding status", ["Never", "Less than 6 months", "6 months regular not exclusively", "6 months exclusively"]),
            "DevDelay_2122": st.selectbox("Developmental delay status", ["Does not have condition", "Ever told, does not currently have", "Currently has condition"]),
            "learning_2122": st.selectbox("Learning disability status", ["Does not have condition", "Ever told, does not currently have", "Currently has condition"])
        })

    with col3:
        input_dict.update({
            "autism_2122": st.selectbox("Autism spectrum disorder status", ["Does not have condition", "Ever told, does not currently have", "Currently has condition"]),
            "BedTime_2122": st.selectbox("Bedtime routine regularity", ["Always", "Usually", "Sometimes", "Rarely or never"]),
            "ACE1more4Com_2122": st.selectbox("Community-based ACEs", ["No ACEs", "1 or more ACEs"]),
            "ACEincome_2122": st.selectbox("Income-based ACEs", ["No ACEs", "Rarely", "Often", "Very Often"]),
            "ACE2more11_2122": st.selectbox("Adverse childhood experiences", ["No Aces", "Single Ace", "Multiple Aces"])
        })

    if st.button("Predict"):
        if 2 <= age <= 17:
            results = predict(input_dict)
            if results:
                st.markdown(f"<div class='predict-bounce'><p style='background-color:#d2f5f3;padding:15px;border-radius:10px;font-size:20px;text-align:center;'>🎯 Prediction Results: <strong>{results}</strong></p></div>", unsafe_allow_html=True)
            else:
                st.error("Prediction could not be made. Please check the input values.")
        else:
            st.error("Please enter an age between 2 and 17 years to proceed.")

    st.markdown("---")
    st.subheader("💬 Need Instant Therapy? Try Our ComfortChat Bot!")
    st.markdown(
        '<iframe width="100%" height="430" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/d0d44173-b514-4a6c-a8c5-39f033bb2b67"></iframe>',
        unsafe_allow_html=True
    )
    st.info("🌿 ADHD is manageable with the right support. If you or someone you know is struggling, consult a medical professional.")

# --- About ADHD ---
elif page == "About ADHD":
    adhd_info.show_adhd_info()

# --- Chill Zone Snake Game ---
elif page == "Chill Zone (Snake Game)":
    st.title("🎮 Chill Zone - Snake Game")
    st.markdown("Use your arrow keys to control the snake 🐍")
    try:
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "snake_embed.html")
        with open(file_path, "r", encoding="utf-8") as file:
            snake_game_html = file.read()
            components.html(snake_game_html, height=600)
    except FileNotFoundError:
        st.error("⚠️ 'snake_embed.html' file not found.")
    except UnicodeDecodeError:
        st.error("⚠️ Unicode error while reading 'snake_embed.html'.")

# --- Mood Booster Zone ---
elif page == "Mood Booster Zone":
    fun_zone()

# --- Coloring Canvas Zone ---
elif page == "Coloring Canvas 🎨":
    coloring_canvas()
