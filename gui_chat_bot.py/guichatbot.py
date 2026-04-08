import tkinter as tk
from tkinter import messagebox
import random
from textblob import TextBlob
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify setup
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='5e3917ad06714e5194d003ca153c6ceb',
    client_secret='c831572b16c84261bce92ba1f4a59ed6'
))

# Emotion detection
def get_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "happy"
    elif polarity < -0.1:
        return "sad"
    else:
        return "chill"

# Song recommendation
def get_song_from_spotify(emotion):
    try:
        emotion_queries = {
            "happy": ["happy mood", "feel good", "uplifting pop", "dance party"],
            "sad": ["sad songs", "emotional ballads", "melancholy vibes", "soft piano"],
            "chill": ["chill vibes", "lofi", "acoustic relax", "easy listening"],
            "angry": ["angry rock", "rage songs", "metal workout", "hardcore rap"]
        }

        query_list = emotion_queries.get(emotion, ["chill vibes"])
        query = random.choice(query_list)

        results = sp.search(q=query, type='track', limit=10)
        tracks = results['tracks']['items']
        if not tracks:
            return "No songs found for that mood."

        track = random.choice(tracks)
        name = track['name']
        artist = track['artists'][0]['name']
        link = track['external_urls']['spotify']
        return f"{name} by {artist}\n{link}"

    except Exception as e:
        return f"Error: {e}"

# Handle submit
def submit_input():
    user_text = user_input.get()
    if user_text.strip() == "":
        messagebox.showwarning("Input Error", "Please enter how you feel.")
        return

    emotion = get_emotion(user_text)
    song = get_song_from_spotify(emotion)
    output_text.set(f"You seem {emotion}.\nRecommended Song:\n{song}")
    user_input.set("")

# GUI setup
root = tk.Tk()
root.title("🎧 Emotion-Based Song Recommender")

root.geometry("450x350")
root.config(bg="#f0f0f0")

tk.Label(root, text="Enter how you're feeling:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

user_input = tk.StringVar()
tk.Entry(root, textvariable=user_input, font=("Arial", 12), width=40).pack(pady=5)

tk.Button(root, text="🎶 Get Song", command=submit_input, font=("Arial", 12), bg="#4caf50", fg="white").pack(pady=10)

output_text = tk.StringVar()
tk.Label(root, textvariable=output_text, wraplength=400, font=("Arial", 12), bg="#f0f0f0", fg="#333").pack(pady=20)

tk.Label(root, text="Made with ❤️ by Krishna", font=("Arial", 9), bg="#f0f0f0", fg="gray").pack(side="bottom", pady=10)

root.mainloop()
