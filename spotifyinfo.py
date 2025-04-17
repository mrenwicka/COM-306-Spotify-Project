import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv

class spotify:
    def __init__(self):
        load_dotenv()

        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.redirect_uri = "http://localhost:8080/callback"

        #Force re-authentication by setting the cache_path to None
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=["user-top-read", "user-read-playback-state", "user-read-currently-playing"],
            cache_path=None  #This ensures no token caching
        ))

    def get_client(self):
        return self.sp
