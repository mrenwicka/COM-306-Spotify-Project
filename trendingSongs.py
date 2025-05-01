import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyTrendingSongs:
    def __init__(self, playlist_id="37i9dQZEVXbMDoHDwVN2tF", limit=10):
        """
        Default playlist_id = Global Top 50
        """
        self.limit = limit
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id="f8f3c96e665648f8823d13c6d2f40617",
            client_secret="f9a65795fb774d3ba5103499a4722901"
        ))
        self.playlist_id = playlist_id

    def get_trending_songs(self):
        results = self.sp.playlist_tracks(self.playlist_id, limit=self.limit)

        trending_tracks = []
        for item in results['items']:
            track = item['track']
            track_info = {
                "id": track['id'],
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "album": track['album']['name'],
                "url": track['external_urls']['spotify'],
                "image": track['album']['images'][0]['url']
            }
            trending_tracks.append(track_info)
        return trending_tracks


if __name__ == "__main__":
    spotify_trending = SpotifyTrendingSongs(limit=5)
    trending_songs = spotify_trending.get_trending_songs()
    for track in trending_songs:
        print(f"{track['name']} by {track['artist']} - {track['url']}")
