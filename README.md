# Chatbot Song Recommender

A simple chatbot application that analyzes your mood from text input and recommends songs from Spotify based on detected emotions.

## Features

- **Emotion Detection**: Uses sentiment analysis to detect if you're feeling happy, sad, or chill.
- **Song Recommendations**: Fetches random songs from Spotify matching your mood.
- **Two Interfaces**: 
  - Command-line interface (CLI) in `main.py`
  - Graphical user interface (GUI) in `gui_chat_bot.py/guichatbot.py` using Tkinter

## Requirements

- Python 3.x
- Spotify Developer Account (for API access)
- Required Python packages: `spotipy`, `textblob`

## Installation

1. Clone or download the repository.

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Ensure you have a Spotify Developer account and obtain your `client_id` and `client_secret`. Update the credentials in the code files if needed (currently hardcoded).

## Usage

### CLI Version
Run the command-line chatbot:
```
python main.py
```
Follow the prompts to enter your name and describe how you're feeling.

### GUI Version
Run the graphical interface:
```
python gui_chat_bot.py/guichatbot.py
```
Enter your feelings in the text box and click "Get Song" to receive a recommendation.

## How It Works

1. The app analyzes the polarity of your input text using TextBlob.
2. Based on the sentiment:
   - Positive (>0.1): Happy
   - Negative (<-0.1): Sad
   - Neutral: Chill
3. Queries Spotify with mood-appropriate search terms.
4. Returns a random song recommendation with artist and Spotify link.

## Notes

- Spotify API credentials are currently hardcoded in the source files. For production use, consider using environment variables or a config file.
- The app requires an active internet connection to fetch songs from Spotify.

## License

This project is for educational purposes. Ensure compliance with Spotify's API terms of service.