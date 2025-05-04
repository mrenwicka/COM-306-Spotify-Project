import spotipy
from collections import Counter
from spotipy.exceptions import SpotifyException

class SpotifyTopSongs:
    def __init__(self, sp_client, time_range="short_term", limit=10, offset=0):
        self.sp = sp_client
        self.time_range = time_range
        self.limit = limit
        self.offset = offset

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

    def your_playlists(self, max_count=2):
        """
        Not every account shares the same playlists apparently so, search through primary
        and fallbacks in the case that the didn't have any in primary
        """
        primary_keywords = [
            "Discover Weekly",
            "On Repeat",
            "Repeat Rewind",
            "Daily Mix 1",
            "Daily Mix 2",
            "Daily Mix 3"
        ]

        fallback_keywords = [
            "Your Mix",
            "Daily Mix",
            "Made For You"
        ]

        found = []

        try:
            
            for name in primary_keywords:
                result = self.sp.search(q=name, type='playlist', limit=1)
                items = result.get('playlists', {}).get('items', [])
                if items and items[0]:
                    playlist = items[0]
                    found.append({
                        "name": playlist['name'],
                        "id": playlist['id'],
                        "url": playlist['external_urls']['spotify'],
                        "image": playlist['images'][0]['url']
                    })
                if len(found) >= max_count:
                    return found
 
            for fallback in fallback_keywords:
                result = self.sp.search(q=fallback, type='playlist', limit=3)
                items = result.get('playlists', {}).get('items', [])
                for playlist in items:
                    if len(found) >= max_count:
                        break
                    found.append({
                        "name": playlist['name'],
                        "id": playlist['id'],
                        "url": playlist['external_urls']['spotify'],
                        "image": playlist['images'][0]['url']
                    })
        except SpotifyException as e:
            print("Searching Error", e)
        except Exception as e:
            print("Random error:", e)

        return found


if __name__ == "__main__":
    from spotifyinfo import spotify
    sp_client = spotify().get_client()
    
    spotify_top = SpotifyTopSongs(sp_client, limit=5)

    top_songs = spotify_top.get_top_songs()
    personal_playlists = spotify_top.your_playlists()

    print("\nTop Tracks:")
    for track in top_songs:
        print(f"{track['name']} by {track['artist']} - {track['url']}")

    print("\nPlaylists:")
    if personal_playlists:
        for p in personal_playlists:
            print(f"{p['name']} - {p['url']}")
