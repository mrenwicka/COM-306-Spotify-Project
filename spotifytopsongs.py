import pip


pip spotipy
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "user-top-read"

SPOTIFY_CLIENT_ID = "f8f3c96e665648f8823d13c6d2f40617"
SPOTIFY_CLIENT_SECRET = "f9a65795fb774d3ba5103499a4722901"
SPOTIFY_REDIRECT_URI = "http://localhost:8080/callback"

# get top tracks
def get_user_top_songs(time_range="medium_term", limit=10, offset=0):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=SCOPE
    ))

    results = sp.current_user_top_tracks(time_range=time_range, limit=limit, offset=offset)

    # data
    top_tracks = []
    for item in results['items']:
        track_info = {
            "name": item['name'],
            "artist": item['artists'][0]['name'],
            "url": item['external_urls']['spotify'],
            "album": item['album']['name'],
            "image": item['album']['images'][0]['url']  # Album cover
        }
        top_tracks.append(track_info)

    ##return top_tracks

    if __name__ == "__main__":
        top_songs = get_user_top_songs()
    for track in top_songs:
        print(f"{track['name']} by {track['artist']} - {track['url']}")

