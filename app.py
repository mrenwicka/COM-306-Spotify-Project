from topsongs import SpotifyTopSongs
from flask import Flask, render_template, redirect, request, session, url_for
from weathertoplaylist import weatherplaylists
from currentsong import SpotifyTrackInfo
from monthlyplaylist import monthlyplaylist
from topsongs import SpotifyTopSongs
from userinfo import userinfo

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect to the login page
    return redirect(url_for('weather'))

@app.route('/topsongs')
def topsongs():
    spotify = SpotifyTopSongs(limit=3)
    top_tracks = spotify.get_top_songs()
    print("DEBUG: top_tracks =", top_tracks)
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

    month_client = monthlyplaylist()
    month = month_client.current_month()
    monthly_playlist_url = month_client.monthly_playlist(month)

    top_songs_client = SpotifyTopSongs(limit=3)
    top_tracks = top_songs_client.get_top_songs()

    user_client = userinfo()
    user_id = user_client.get_user_id()
    username = user_client.get_username(user_id)
    profile_pic = user_client.get_profile_pic(user_id)
    

    return render_template('index.html', weather_playlist_url=weather_playlist_url, song_info=song_info, 
                           monthly_playlist_url=monthly_playlist_url, top_tracks=top_tracks, username = username,
                           profile_pic = profile_pic)



if __name__ == '__main__':
    app.run(debug=True)
