from folium import Map
from geo import Geopoint

lat = float("32.98220")
long = float("-96.53060")

antipode_lat = lat.__mul__(int("-1"))

antipode_long = long.__add__(float("180"))

if long.__lt__(float("0")):
    antipode_long = long.__add__(float("180"))
elif long.__eq__(float("0")):
    antipode_long = float("180")
else:
    antipode_long = long.__sub__(float("180"))

print(antipode_lat, antipode_long)

location = list((antipode_lat, antipode_long))

# mymap = Map(location)
# mymap.save(str("antipode_nathy.html"))

g = Geopoint(2, 4)

print(g.closest_parallel())