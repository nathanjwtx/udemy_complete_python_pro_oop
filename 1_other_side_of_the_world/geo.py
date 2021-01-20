from datetime import datetime
from datetime import tzinfo
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather


class Geopoint:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.weather_api = '15aab1e65a6d9fb14489bad5a8c5e883'

    def closest_parallel(self):
        return round(self.latitude)

    def get_time(self):
        tz_str = TimezoneFinder().timezone_at(lat=self.latitude, lng=self.longitude)
        tz_now = datetime.now(timezone(tz_str))
        return tz_now

    def get_weather(self):
        return Weather(self.weather_api, lat=self.latitude, lon=self.longitude).next_12h()


karachi = Geopoint(24.850134, 67.032592)
print(karachi.closest_parallel())
print(karachi.get_time())
print(karachi.get_weather())
