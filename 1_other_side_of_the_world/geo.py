from datetime import datetime
from random import uniform

from folium import Marker
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather


class Geopoint(Marker):

    # class variables
    lat_range = (-90, 90)
    long_range = (-180, 180)

    # the popup is now being directly added via the Popup type from folium in main2.py
    # def __init__(self, latitude, longitude, popup=None):
    #     # instance variables
    #     super().__init__(location=[latitude, longitude], popup=popup)
    #     self.latitude = latitude
    #     self.longitude = longitude
    #     self.weather_api = '15aab1e65a6d9fb14489bad5a8c5e883'

    def __init__(self, latitude, longitude):
        # instance variables
        super().__init__(location=[latitude, longitude])
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
        return Weather(self.weather_api, lat=self.latitude, lon=self.longitude).next_12h_simplified()

    @classmethod
    def random(cls):
        return cls(latitude=uniform(-90, 90), longitude=uniform(-180, 180))


karachi = Geopoint(24.850134, 67.032592)
# print(karachi.closest_parallel())
# print(karachi.get_time())
# print(karachi.get_weather())
