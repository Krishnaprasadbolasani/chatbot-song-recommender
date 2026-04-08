import random
from textblob import TextBlob
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='5e3917ad06714e5194d003ca153c6ceb',
    client_secret='c831572b16c84261bce92ba1f4a59ed6'
))


def get_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "happy"
    elif polarity < -0.1:
        return "sad"
    else:
        return "chill"  # neutral mood

#getting songs from

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

        # Search with limit=10 for variety
        results = sp.search(q=query, type='track', limit=10)
        tracks = results['tracks']['items']

        if not tracks:
            return "😕 Sorry, no songs found for that emotion."

        # Randomly select one from the results
        track = random.choice(tracks)
        name = track['name']
        artist = track['artists'][0]['name']
        link = track['external_urls']['spotify']
        return f"🎵 {name} by {artist}\n🔗 {link}"

    except Exception as e:
        return f"⚠️ Error fetching song: {e}"

#chat bot
def chatbot():
    print("🎧 Melody: Hi! I’m your song buddy.")
    name = input("🎤 What's your name? ")

    print(f"\n👋 Nice to meet you, {name}!")
    print("Tell me how you're feeling today. (Type 'exit' to quit)\n")

    while True:
        user_input = input(f"{name}: ")

        if user_input.strip() == "":
            print("Melody: Please tell me how you're feeling 🙈")
            continue

        if user_input.lower() == "exit":
            print(f"\nMelody: Bye {name}! Stay tuned and take care 🎶")
            break

        emotion = get_emotion(user_input)
        song = get_song_from_spotify(emotion)

        print(f"\nMelody: You seem *{emotion}*. Here's a song for you:")
        print(song)
        print("\n" + "-"*50 + "\n")

# ====== RUN THE CHATBOT ======
if __name__ == "__main__":
    chatbot()
