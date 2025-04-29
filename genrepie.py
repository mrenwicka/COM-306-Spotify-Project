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

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Top Genres")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    
    return filename
