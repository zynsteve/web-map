import folium
import pandas

data = pandas.read_csv("world_volcanoes.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
elev = list(data["Elev"])
name = list(data['Volcano Name'])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=4, popup=name+", "+str(el)+"m",
    fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Poputation")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")
