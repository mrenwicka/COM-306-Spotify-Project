import time
import spotipy
from spotifyinfo import spotify

class SpotifyTrackInfo:
    def __init__(self):
        self.sp = spotify().get_client()
        self.last_track_id = None

    # def authenticate(self):
    #     # Check if token is cached
    #     token_info = self.sp_oauth.get_cached_token()
    #     if token_info:
    #         self.sp = spotipy.Spotify(auth=token_info['access_token'])
    #         return None
    #     return self.sp_oauth.get_authorize_url()

    def get_current_song_info(self):
        current = self.sp.current_playback()
        if not current or not current.get("is_playing"):
            return None

        track = current["item"]
        track_id = track["id"]
        if track_id != self.last_track_id:
            self.last_track_id = track_id
            song_name = track["name"]
            artist_name = ", ".join([artist["name"] for artist in track["artists"]])
            album_name = track["album"]["name"]
            album_cover_url = track["album"]["images"][0]["url"]
            return {
                "song": song_name,
                "artist": artist_name,
                "album": album_name,
                "cover_url": album_cover_url
            }
        return "same"

if __name__ == "__main__":
    spotify_info = SpotifyTrackInfo()
    while True:
        song_info = spotify_info.get_current_song_info()
        if song_info:
            print(song_info)
        time.sleep(5)  # Delay to avoid too many API requests
