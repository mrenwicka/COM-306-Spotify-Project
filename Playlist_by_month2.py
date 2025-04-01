
class monthlyplaylist:
    def monthly_playlist(self):
# Define playlists for each month
        MONTHLY_PLAYLISTS = {
        'January': '37i9dQZF1E8SOYK9xNEau6',
        'February': '37i9dQZF1E8P7g6lqWVri1',
        'March': '37i9dQZF1E8P1VNngOw2qN',
        'April': '37i9dQZF1E8Kw2z1JLhOLE',
        'May': '37i9dQZF1E4nsatZeLaAok',
        'June': '37i9dQZF1E8ODvgNaj9jxM',
        'July': '37i9dQZF1E8AhnyEbQCRqq',
        'August': '37i9dQZF1E8TwrQ3SDu4qi',
        'September': '37i9dQZF1E8KixPw8XwHmu',
        'October': '37i9dQZF1E8ECtSJBzd2nA',
        'November': '37i9dQZF1E8BGvhVA1Khrl',
        'December': '37i9dQZF1E8OSswGcqKz7M',
        }

        current_month = datetime.datetime.now().strftime('%B')

        monthly_playlist_uri = MONTHLY_PLAYLISTS.get(current_month, None)

        return f"https://open.spotify.com/embed/playlist/{monthly_playlist_uri}"

