import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()


SPOTIFY_CLIENT_ID = os.getenv('CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:8080/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
client_secret=SPOTIFY_CLIENT_SECRET,
redirect_uri=SPOTIFY_REDIRECT_URI,
scope=["user-top-read"]))

def get_artist_top_songs():
    list = []
    result = sp.search(q="Amy Winehouse", type = "artist", limit = 1)
    artist_id = result["artists"]["items"][0]["id"]
    tracks = sp.artist_top_tracks(artist_id)
    for track in tracks["tracks"][:5]:
        list.append(track["name"])
    return list

def get_user_top_songs():
    list = []
    results = sp.current_user_top_tracks(time_range='long_term', limit=10)
    for track in results["items"]:
        list.append(track["name"])
    return list

@app.route('/')
def hi():
    songs = get_user_top_songs()
    return render_template('index.html', text = songs)



if __name__ == '__main__':
    app.run(debug=True)