import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from collections import Counter
import os
from spotifyinfo import spotify

def generate_genre_pie_chart(filename='static/genre_chart.png', limit=50, time_range='medium_term'):
    sp = spotify().get_client()
    top_artists = sp.current_user_top_artists(limit=limit, time_range=time_range)

    genre_list = []
    for artist in top_artists['items']:
        genre_list.extend(artist['genres'])

    if not genre_list:
        return None 

    genre_counts = Counter(genre_list)
    top_genres = genre_counts.most_common(7)
    labels, sizes = zip(*top_genres)

    plt.figure(figsize=(6, 6), facecolor='#16243b')
    ax = plt.gca()
    ax.set_facecolor('#16243b')
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'color': 'white'})
    plt.title("Top Genres", color='white')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(filename, facecolor='#0d1117')
    plt.close()

    
    return filename

def generate_artist_pie_chart(filename='static/artist_chart.png', limit=50, time_range='medium_term'):
    sp = spotify().get_client()
    
    #get user's top tracks
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    if not top_tracks['items']:
        return None

    #how many tracks artist appears in
    from collections import Counter
    artist_counts = Counter()

    for track in top_tracks['items']:
        for artist in track['artists']:
            artist_counts[artist['name']] += 1

    #keeping only top artists
    top_artists = artist_counts.most_common(7)
    labels, sizes = zip(*top_artists)

    plt.figure(figsize=(6, 6), facecolor='#0d1117')
    ax = plt.gca()
    ax.set_facecolor('#0d1117')
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'color': 'white'})
    plt.title("Top Artists (by track count)", color='white')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(filename, facecolor='#0d1117')
    plt.close()

    return filename
