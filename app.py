import streamlit as st
from pydub import AudioSegment
import tempfile
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Google API for audio summarization
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def summarize_audio(audio_file_path):
    """Summarize the audio using Google's Generative API."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    audio_file = genai.upload_file(path=audio_file_path)
    response = model.generate_content(
        [
            "Please summarize the following audio.",
            audio_file
        ]
    )
    return response.text

def save_uploaded_file(uploaded_file):
    """Save uploaded file to a temporary file and return the path."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        st.error(f"Error handling uploaded file: {e}")
        return None

# Streamlit app interface
st.set_page_config(page_title="Audio Summarization App", page_icon="🔊", layout="wide")

st.title('🎙️ Audio Summarization App')

with st.expander("About this app", expanded=True):
    st.write("""
        This app leverages Google's Generative AI to provide concise summaries of your audio files. 
        Simply upload an audio file in WAV or MP3 format, and get a summary of its content in just a few moments. 
        🎧 Enjoy a better understanding of your audio content!
    """)

col1, col2 = st.columns([2, 1])

with col1:
    audio_file = st.file_uploader("Upload Your Audio File", type=['wav', 'mp3'], label_visibility="visible")

with col2:
    st.markdown("""
        <style>
        .css-1d391kg { font-size: 16px; }
        </style>
        """, unsafe_allow_html=True)
    st.write("🔊 Supported Formats: WAV, MP3")

if audio_file is not None:
    audio_path = save_uploaded_file(audio_file)  # Save the uploaded file and get the path
    st.audio(audio_path)

    if st.button('Summarize Audio', key='summarize_button'):
        with st.spinner('Summarizing...'):
            summary_text = summarize_audio(audio_path)
            st.subheader("Summary:")
            st.write(summary_text)

            # Downloadable option
            st.download_button(
                label="Download Summary",
                data=summary_text,
                file_name="audio_summary.txt",
                mime="text/plain",
                help="Click to download the summary text file"
            )

# Add a footer with a simple message
st.markdown("""
    <style>
    .footer {
        position: absolute;
        bottom: 0;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: gray;
    }
    </style>
    <div class="footer">
        Developed with ❤️ by [Ranjesh Kumar Verma]
    </div>
    """, unsafe_allow_html=True)
