import streamlit as st
import streamlit.components.v1 as components

def coloring_canvas():
    st.markdown("""
        <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            background: linear-gradient(to right, #00bfa5, #007d8a);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
        .canvas-container {
            display: flex;
            justify-content: center;
            padding: 20px;
        }
        iframe {
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🖌️ Coloring Canvas - Relax & Express!</div>", unsafe_allow_html=True)
    st.markdown("Coloring can help reduce stress, increase focus, and boost creativity. Choose colors and paint freely!")

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container():
        components.html(
            """
            <div class="canvas-container">
                <iframe src="https://paint.toys/" width="100%" height="600px"></iframe>
            </div>
            """,
            height=620,
            scrolling=False
        )
