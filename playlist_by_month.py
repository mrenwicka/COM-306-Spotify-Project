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

def test():
    months = [January,February,March]


