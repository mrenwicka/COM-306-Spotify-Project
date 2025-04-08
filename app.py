import os

from flask import Flask, render_template, redirect, request, session, url_for
from weathertoplaylist import weatherplaylists

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
        
        # Read the logins.txt file to check for a match
        with open("logins.txt", 'r') as file:
            logins = file.readlines()

        # Check if there is a matching username and password
        for login in logins:
            stored_username, stored_password = login.strip().split(', ')  # Split the line into username and password
            
            # Check if the username and password match
            stored_username = stored_username.split(': ')[1]  # Extract the username part
            stored_password = stored_password.split(': ')[1]  # Extract the password part
            
            if stored_username == username and stored_password == password:
                # If a match is found, redirect to the weather page or another page
                return redirect(url_for('weather'))
        
        # If no match is found, you can display an error message or return to the login page
        error_message = "Invalid username or password!"
        return render_template('login.html', error_message=error_message)

    # If it's a GET request, render the login page
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the login details from the form
        username = request.form['username']
        password = request.form['password']
        
        # Write login details to a text file
        with open("logins.txt", 'a') as file:
            file.write(f'Username: {username}, Password: {password}\n')
        
        return redirect(url_for('login'))
    
    # If it's a GET request, render the login page
    return render_template('register.html')



@app.route('/dashboard')
def dashboard():
    spotify = spotify()
    song_info = spotify.get_current_song_info()

    if song_info == "same":
        song_info = None

    return render_template('index.html', song_info=song_info)



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
