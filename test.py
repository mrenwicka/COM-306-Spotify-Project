import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template

app = Flask(__name__)


SPOTIFY_CLIENT_ID = "f8f3c96e665648f8823d13c6d2f40617"
SPOTIFY_CLIENT_SECRET = "f9a65795fb774d3ba5103499a4722901"
SPOTIFY_REDIRECT_URI = "http://localhost:8080/callback"

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