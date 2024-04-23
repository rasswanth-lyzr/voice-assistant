import os

import streamlit as st
from dotenv import load_dotenv
from lyzr import VoiceBot

load_dotenv()

AUDIO_FILE_NAME = "tts_output.mp3"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.write("Voice Options : [LINK](https://platform.openai.com/docs/guides/text-to-speech/voice-options)")

voice_model = st.radio("Choose Voice",["alloy", "echo", "fable", "onyx", "nova", "shimmer"])
st.header("Enter your caption")
input_caption = st.text_area("Enter caption", label_visibility="hidden")
submit_button = st.button("Submit")

if submit_button:
    vb = VoiceBot(api_key=OPENAI_API_KEY, voice=voice_model)
    vb.text_to_speech(input_caption)
    st.audio(AUDIO_FILE_NAME, format="audio/mpeg", loop=False)