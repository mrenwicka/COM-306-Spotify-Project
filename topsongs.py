import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyTopSongs:
    def __init__(self, time_range="short_term", limit=10, offset=0):
        self.time_range = time_range
        self.limit = limit
        self.offset = offset
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id="f8f3c96e665648f8823d13c6d2f40617",
            client_secret="f9a65795fb774d3ba5103499a4722901",
            redirect_uri="http://localhost:8080/callback",
            scope="user-top-read"
        ))

    def get_top_songs(self):
        results = self.sp.current_user_top_tracks(
            time_range=self.time_range,
            limit=self.limit,
            offset=self.offset
        )

        top_tracks = []
        for item in results['items']:
            track_info = {
                "id": item['id'],
                "name": item['name'],
                "artist": item['artists'][0]['name'],
                "album": item['album']['name'],
                "url": item['external_urls']['spotify'],
                "image": item['album']['images'][0]['url']
            }
            top_tracks.append(track_info)
        return top_tracks


if __name__ == "__main__":
    spotify_top = SpotifyTopSongs(limit=3)
    top_songs = spotify_top.get_top_songs()
    for track in top_songs:
        print(f"{track['name']} by {track['artist']} - {track['url']}")
