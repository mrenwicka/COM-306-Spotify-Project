import openmeteo_requests
import requests_cache
from retry_requests import retry

class weather:
    def __init__(self, lat=41.355423, long=-72.102760):
        self.latitude = lat
        self.longitude = long
        self.url = "https://api.open-meteo.com/v1/forecast"

        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        self.client = openmeteo_requests.Client(session=retry_session)

    def get_weather(self): 
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude, 
            "current": ["weather_code"],
        }

        responses = self.client.weather_api(self.url, params=params)
        response = responses[0]
        current = response.Current()

        weather_data = {
            "weather_code": current.Variables(0).Value()
        }

        return list(weather_data.values())[0]

if __name__ == "__main__":
    client = weather()
    weather_code = client.get_weather()
    print(weather_code)



