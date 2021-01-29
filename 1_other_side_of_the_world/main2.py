from folium import Map, Popup
from geo import Geopoint

latitude = 24.850134
longitude = 67.032592

mymap = Map(location=[latitude, longitude])

geopoint = Geopoint(latitude, longitude)

popup = Popup(str(geopoint.get_weather()[0]))
popup.add_to(geopoint)

geopoint.add_to(mymap)

mymap.save('map.html')
