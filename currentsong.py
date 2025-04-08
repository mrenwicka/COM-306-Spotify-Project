import time
import os
from spotifyinfo import SpotifyClient


 self.last_track_id = None

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
    spotify = SpotifyClient()

