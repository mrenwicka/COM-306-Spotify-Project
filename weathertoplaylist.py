from currentweather import weather

class weatherplaylists:
    def __init__(self):
        self.weather = weather()

    def get_weather(self):
        return self.weather.get_weather()
    
    def get_weather_playlist(self, weather_code):
        clear_skies = "4mmm21hgSSxbfPuZLOJAhF" #0
        partly_cloudy = "0FmM13TH611hzgvwM7j9uQ" #1,2,3
        foggy = "5R3IqV2qHAgXl7qDpw2tLH" #45,48
        drizzle = "5ilG4FeWNvuzyh1LwxmxIr" #51,53,55,56,57
        rainy = "47S4MBG0EEXwA0GdJUA4Ur" #61,63,65,66,67
        snowy = "7bFSWgWheCLGmVDiTkOKPY" #71,73,75,77
        pouring = "6OFZElgLXsPRIJh2ngKTnp" #80,81,82
        blizzard = "3ZRsbTZrT1cwfBvCg1QdF4" #85,86
        thunderstorm = "6riD5QU5aPboCO7pAfZVRN" #95,96,99
        playlist_ids = {
            clear_skies: [0],
            partly_cloudy: [1, 2, 3],
            foggy: [45, 48],
            drizzle: [51, 53, 55, 56, 57],
            rainy: [61, 63, 65, 66, 67],
            snowy: [71, 73, 75, 77],
            pouring: [80, 81, 82],
            blizzard: [85, 86],
            thunderstorm: [95, 96, 99],
        }

        for id, code in playlist_ids.items():
            if weather_code in code:
                return id

        return "37i9dQZEVXbLRQDuF5jeBp"
    
    def get_playlist_url(self, playlist_id):
        return f"https://open.spotify.com/embed/playlist/{playlist_id}"


    
if __name__ == "__main__":
    weather_client = weatherplaylists()
    weather_code = weather_client.get_weather()

    playlist_id = weather_client.get_weather_playlist(weather_code)
    playlist_url = weather_client.get_playlist_url(playlist_id)
    
    print(playlist_id)
    print(playlist_url)
