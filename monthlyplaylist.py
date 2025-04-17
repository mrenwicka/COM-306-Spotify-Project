import datetime

class monthlyplaylist:
    def current_month(self):
        current_month = datetime.datetime.now().strftime('%B')
        return current_month

    def monthly_playlist(self, currentmonth):
# Define playlists for each month
        playlist_ids = {
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

        monthly_playlist_url = playlist_ids.get(currentmonth)

        return f"https://open.spotify.com/embed/playlist/{monthly_playlist_url}"

if __name__ == "__main__":
    month_client = monthlyplaylist()
    currentmonth = month_client.current_month()
    playlist_id = month_client.monthly_playlist(currentmonth)
    print(playlist_id)

