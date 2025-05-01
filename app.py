from topsongs import SpotifyTopSongs
from flask import Flask, render_template, redirect, request, session, url_for
from weathertoplaylist import weatherplaylists
from currentsong import SpotifyTrackInfo
from monthlyplaylist import monthlyplaylist
from topsongs import SpotifyTopSongs
from userinfo import userinfo
from genrepie import generate_genre_pie_chart, generate_artist_pie_chart

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect to the login page
    return redirect(url_for('weather'))

@app.route('/stats')
def stats():
    spotify = SpotifyTrackInfo()

    user_client = userinfo()
    user_id = user_client.get_user_id()
    username = user_client.get_username(user_id)
    profile_pic = user_client.get_profile_pic(user_id)

    top_songs_client = SpotifyTopSongs(limit=3)
    top_tracks = top_songs_client.get_top_songs()

    genre_chart_path = generate_genre_pie_chart()
    artist_chart_path = generate_artist_pie_chart()

    return render_template('stats.html',
                           top_tracks=top_tracks,
                           username=username,
                           profile_pic=profile_pic,
                           genre_chart_url=genre_chart_path,
                           artist_chart_url=artist_chart_path)
    

@app.route('/home')
def weather():
    weather = weatherplaylists()
    spotify = SpotifyTrackInfo()

    user_client = userinfo()
    user_id = user_client.get_user_id()
    username = user_client.get_username(user_id)
    profile_pic = user_client.get_profile_pic(user_id)

    song_info = spotify.get_current_song_info()
    if song_info == "same":
        song_info = None

    weather_code = weather.get_weather()
    playlist_id = weather.get_weather_playlist(weather_code)
    weather_playlist_url = weather.get_playlist_url(playlist_id)

    month_client = monthlyplaylist()
    month = month_client.current_month()
    monthly_playlist_url = month_client.monthly_playlist(month)
    
    

    return render_template('index.html',
                           weather_playlist_url=weather_playlist_url,
                           song_info=song_info,
                           monthly_playlist_url=monthly_playlist_url,
                           username=username,
                           profile_pic=profile_pic,)



if __name__ == '__main__':
    app.run(debug=True)
