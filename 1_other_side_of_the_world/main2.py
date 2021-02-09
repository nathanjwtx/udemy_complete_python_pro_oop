from folium import Map, Popup
from geo import Geopoint

# karachi
# latitude = 24.850134
# longitude = 67.032592

# wylie
latitude = 32.98226
longitude = -96.53057

mymap = Map(location=[latitude, longitude])


geopoint = Geopoint(latitude, longitude)

forecast = geopoint.get_weather()

popup_content = f"""
{forecast[0][0][-8:-6]}: {round(forecast[0][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width="35">
<hr style="margin:1px">
{forecast[1][0][-8:-6]}: {round(forecast[1][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width="35">
<hr style="margin:1px">
{forecast[2][0][-8:-6]}: {round(forecast[2][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width="35">
<hr style="margin:1px">
{forecast[3][0][-8:-6]}: {round(forecast[3][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width="35">
<hr style="margin:1px">
"""

# popup = Popup(str(geopoint.get_weather()[0]))
popup = Popup(popup_content, max_width=400)
popup.add_to(geopoint)

geopoint.add_to(mymap)

mymap.save('map.html')
