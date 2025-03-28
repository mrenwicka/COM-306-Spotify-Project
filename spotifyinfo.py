import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

class spotify:
    def __init__(self):
        load_dotenv()

        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.redirect_uri = "http://localhost:8080/callback"

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=["user-top-read"]
        ))