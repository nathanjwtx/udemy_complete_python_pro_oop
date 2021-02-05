from folium import Map, Popup
from geo import Geopoint

latitude = 24.850134
longitude = 67.032592

mymap = Map(location=[latitude, longitude])

popup_content = """
12: 70°F <img src="http://openweathermap.org/img/wn/10d@2x.png" width="35">
<hr style="margin:1px">
12: 70°F <img src="http://openweathermap.org/img/wn/10d@2x.png" width="35">
<hr style="margin:1px">
12: 70°F <img src="http://openweathermap.org/img/wn/10d@2x.png" width="35">
<hr style="margin:1px">
12: 70°F <img src="http://openweathermap.org/img/wn/10d@2x.png" width="35">
<hr style="margin:1px">
"""

geopoint = Geopoint(latitude, longitude)

# popup = Popup(str(geopoint.get_weather()[0]))
popup = Popup(popup_content, max_width=400)
popup.add_to(geopoint)

geopoint.add_to(mymap)

mymap.save('map.html')
