import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[36, -96],zoom_start=4.3, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+" m",
    fill_color=color_producer(el), color='grey', fill_opacity=0.7))

map.add_child(fg)

map.save("Map.html")
