from topsongs import SpotifyTopSongs
from flask import Flask, render_template, redirect, request, session, url_for
from weathertoplaylist import weatherplaylists
from currentsong import SpotifyTrackInfo
from monthlyplaylist import monthlyplaylist

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect to the login page
    return redirect(url_for('weather'))

@app.route('/topsongs')
def topsongs():
    spotify = SpotifyTopSongs()
    top_tracks = spotify.get_top_tracks(limit=3)

    return render_template('topsongs.html', top_tracks=top_tracks)

@app.route('/weather')
def weather():
    weather = weatherplaylists()
    spotify = SpotifyTrackInfo()

    song_info = spotify.get_current_song_info()
    if song_info == "same":
        song_info = None

    weather_code = weather.get_weather()
    playlist_id = weather.get_weather_playlist(weather_code)
    weather_playlist_url = weather.get_playlist_url(playlist_id)

    monthly_playlist_url = monthlyplaylist.monthly_playlist()
    

    return render_template('index.html', weather_playlist_url=weather_playlist_url, song_info=song_info, monthly_playlist_url=monthly_playlist_url)


if __name__ == '__main__':
    app.run(debug=True)
