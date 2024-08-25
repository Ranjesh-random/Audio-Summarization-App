# 🎙️ Audio Summarization App

This Streamlit application leverages Google's Generative AI to provide concise summaries of audio files. By uploading an audio file in WAV or MP3 format, you can receive a summarized text of its content in just a few moments. The app is designed to make it easy to understand the essence of your audio recordings without listening to the entire file.

## Features

- **Audio File Upload:** Supports WAV and MP3 formats.
- **Google Generative AI Integration:** Utilizes Google's Gemini model to generate summaries of uploaded audio files.
- **Download Summary:** Provides an option to download the generated summary as a text file.
- **User-Friendly Interface:** Simple and intuitive layout using Streamlit.

## Installation

To run this app locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/audio-summarization-app.git
    cd audio-summarization-app
    ```

2. **Install the required dependencies:**

    Make sure you have Python 3.7 or higher installed. Then, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Google Generative AI API:**

    - Obtain your API key from Google Generative AI.
    - Create a `.env` file in the root directory and add your API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

4. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the app in your browser at `http://localhost:8501`.
2. Upload an audio file (WAV or MP3 format).
3. Click the **Summarize Audio** button.
4. View the summary directly on the page.
5. Optionally, download the summary as a text file.

## Project Structure

```plaintext
audio-summarization-app/
│
├── app.py                 # Main application script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables file (not included in the repo)
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
