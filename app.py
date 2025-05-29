
import streamlit as st

st.set_page_config(page_title="PariNuma", page_icon="🎨", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #222222;
        color: white;
    }
    .stButton>button {
        background-color: #444444;
        color: white;
        border-radius: 10px;
        padding: 10px;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("PariNuma")
st.markdown("### Welcome to PariNuma — Where Your Feelings Paint the World.")

user_input = st.text_input("Enter your feelings in English:")

if user_input:
    positive_words = ["happy", "joy", "love", "excited", "wonderful", "amazing", "good"]
    negative_words = ["sad", "angry", "bad", "terrible", "hate", "upset"]

    score = 0
    for word in positive_words:
        if word in user_input.lower():
            score += 1
    for word in negative_words:
        if word in user_input.lower():
            score -= 1

    if score > 0:
        emotion = "Positive"
        style = "Abstract"
        palette = "Warm colors (reds, oranges, yellows)"
    elif score < 0:
        emotion = "Negative"
        style = "Expressionist"
        palette = "Cool colors (blues, purples)"
    else:
        emotion = "Neutral"
        style = "Minimalist"
        palette = "Monochrome (black, white, gray)"

    st.markdown(f"**Detected emotion:** {emotion}")
    st.markdown(f"**Suggested style:** {style}")
    st.markdown(f"**Suggested color palette:** {palette}")
