#app.py
from topsongs import SpotifyTopSongs
from spotifyinfo import spotify
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
    # Redirect to the login pageç
    return redirect(url_for('weather'))

@app.route('/stats')
def stats():
    spotify_info = SpotifyTrackInfo()

    user_client = userinfo()
    user_id = user_client.get_user_id()
    username = user_client.get_username(user_id)
    profile_pic = user_client.get_profile_pic(user_id)

    sp_client = spotify().get_client()
    top_songs_client = SpotifyTopSongs(sp_client, limit=3)
    top_tracks = top_songs_client.get_top_songs()

    personal_playlists = top_songs_client.your_playlists(max_count=2)
    playlist_1 = personal_playlists[0] if len(personal_playlists) > 0 else None
    playlist_2 = personal_playlists[1] if len(personal_playlists) > 1 else None

    genre_chart_path = generate_genre_pie_chart()
    artist_chart_path = generate_artist_pie_chart()

    return render_template('stats.html',
                           top_tracks=top_tracks,
                           username=username,
                           profile_pic=profile_pic,
                           genre_chart_url=genre_chart_path,
                           artist_chart_url=artist_chart_path,
                           playlist_1 = playlist_1,
                           playlist_2 = playlist_2)
    

@app.route('/home')
def weather():
    weather = weatherplaylists()
    spotify_info = SpotifyTrackInfo()

    user_client = userinfo()
    user_id = user_client.get_user_id()
    username = user_client.get_username(user_id)
    profile_pic = user_client.get_profile_pic(user_id)

    song_info = spotify_info.get_current_song_info()
    if song_info == "same":
        song_info = None

    weather_code = weather.get_weather()
    playlist_id = weather.get_weather_playlist(weather_code)
    weather_playlist_url = weather.get_playlist_url(playlist_id)

    month_client = monthlyplaylist()
    month = month_client.current_month()
    monthly_playlist_url = month_client.monthly_playlist(month)


    sp_client = spotify().get_client()
    top_songs_client = SpotifyTopSongs(sp_client, limit=3)

    personal_playlists = top_songs_client.your_playlists(max_count=2)
    playlist_1 = personal_playlists[0] if len(personal_playlists) > 0 else None
    playlist_2 = personal_playlists[1] if len(personal_playlists) > 1 else None

    return render_template('index.html',
                           weather_playlist_url=weather_playlist_url,
                           song_info=song_info,
                           monthly_playlist_url=monthly_playlist_url,
                           username=username,
                           profile_pic=profile_pic,
                            playlist_1 = playlist_1,
                           playlist_2 = playlist_2)



if __name__ == '__main__':
    app.run(debug=True)
