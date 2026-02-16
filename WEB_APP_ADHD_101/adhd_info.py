import streamlit as st
import streamlit.components.v1 as components
import os


def show_adhd_info():
    # Apply styling for animation and button effects
    st.markdown("""
        <style>
        .fade-in {
            animation: fadeIn 2s ease-in-out;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }

        .predict-button {
            background: linear-gradient(to right, #007d8a, #005f66);
            border: none;
            color: white;
            padding: 12px 30px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 25px;
            font-family: 'Segoe UI', sans-serif;
            transition: transform 0.3s ease;
        }

        .predict-button:hover {
            background: #004d4d;
            transform: scale(1.05);
        }

        .center {
            display: flex;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with fade-in effect
    st.markdown("<h1 class='fade-in' style='color:#003d4d;'>Understanding ADHD in Children</h1>", unsafe_allow_html=True)

    # Display First Image
    adhd_image_1 = r"F:\Spring 2025\499B\WEB_APP_ADHD_101\ADHD_22.jpg"
    adhd_image_2 = r"F:\Spring 2025\499B\WEB_APP_ADHD_101\ADHD.jpg"

    if os.path.exists(adhd_image_1):
        st.image(adhd_image_1, caption="Signs and Symptoms of ADHD", use_column_width=True)
    else:
        st.warning("⚠️ Image ADHD_22.jpg not found! Please check the file path.")

    # ADHD Explanation
    st.markdown("""
    <div class='fade-in' style="text-align: justify; font-size:18px;">
        <b>ADHD (Attention Deficit Hyperactivity Disorder)</b> is a neurodevelopmental condition 
        that affects a child’s ability to focus, control impulses, and regulate energy levels.
        It impacts academic performance, social interactions, and emotional well-being.
    </div>
    """, unsafe_allow_html=True)

    # ADHD Symptoms
    st.subheader("Common Symptoms of ADHD")
    st.markdown("""
    - **Inattention:** Difficulty focusing, forgetfulness, making careless mistakes.
    - **Hyperactivity:** Excessive movement, difficulty sitting still, fidgeting.
    - **Impulsivity:** Interrupting conversations, acting without thinking, trouble waiting turns.
    - **Emotional Dysregulation:** Mood swings, frustration, and difficulty handling emotions.
    """)

    # Display Second Image
    if os.path.exists(adhd_image_2):
        st.image(adhd_image_2, caption="Challenges of ADHD in School", use_column_width=True)
    else:
        st.warning("⚠️ Image ADHD.jpg not found! Please check the file path.")

    # Causes and Risk Factors
    st.subheader("Causes and Risk Factors")
    st.markdown("""
    While the exact cause of ADHD is unknown, research suggests that a combination of genetic, environmental, 
    and neurological factors play a role. Some risk factors include:

    - **Genetics:** Family history of ADHD or related conditions.
    - **Brain Structure & Function:** Differences in neurotransmitter activity and brain regions responsible for focus.
    - **Prenatal Factors:** Exposure to nicotine, alcohol, or environmental toxins during pregnancy.
    - **Early Childhood Trauma:** Adverse childhood experiences (ACEs) can increase the risk of ADHD.
    """)

    # ADHD Management and Treatment
    st.subheader("How to Manage ADHD?")
    st.markdown("""
    Managing ADHD involves a combination of **behavioral strategies, lifestyle changes, 
    therapy, and medication** based on the severity of symptoms. Some helpful approaches include:

    ✅ **Behavioral Therapy:** Helps children develop coping mechanisms to improve focus and emotional regulation.  
    ✅ **Medication:** Stimulants like methylphenidate (Ritalin) and amphetamines (Adderall) can help.  
    ✅ **Healthy Routine:** Regular sleep, a structured schedule, and a balanced diet improve attention and energy levels.  
    ✅ **Parental Support & School Accommodations:** Special education programs, IEPs, and positive reinforcement.  
    """)

    # Chatbot Integration
    st.subheader("💬 Need Instant Therapy? Talk to Our Chatbot!")
    chatbot_html = '<iframe width="350" height="430" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/d0d44173-b514-4a6c-a8c5-39f033bb2b67"></iframe>'
    components.html(chatbot_html, height=450)

    st.success("🌟 ADHD is manageable with the right support. If you or someone you know is struggling, consult a medical professional!")

    # Redirect button to prediction page
    st.markdown("""
    <div class="center">
        <form action="/" method="get">
            <button class="predict-button" type="submit">✨ Predict Now</button>
        </form>
    </div>
    """, unsafe_allow_html=True)
