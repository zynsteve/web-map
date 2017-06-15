import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[36, -96],zoom_start=4.3, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map.html")
