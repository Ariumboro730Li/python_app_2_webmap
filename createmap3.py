import folium
import pandas
import random

df = pandas.read_csv("Volcanoes.txt")

dfone = df.loc[1]
map = folium.Map(location = [dfone.LAT, dfone.LON], 
    zoom_start=3, 
    tiles="Stamen Terrain"
)
 
fg = folium.FeatureGroup(name="My Map")

lattiude = list(df.LAT)
longitude = list(df.LON)
elevation = list(df.ELEV)
name = list(df.NAME)

def color_producer(elev):
    if elev < 1000:
        color = "green"
    # elif ((elev > 1000) and (elev < 2000)):
    elif 1000 < elev < 2000:
        color = "blue"
    # elif ((elev > 2000) and (elev < 2500)):
    elif 2000 < elev < 2500:
        color = "darkpurple"
    elif elev > 3000:
        color = "beige"
    else:
        color = "red"  
    
    return color;


for lat, lon, elev, name in zip(lattiude, longitude, elevation, name):  
    coordinate = [lat, lon]
    html = f"""<h4>Volcano information:</h4>
    <p>Volcano name: <a href="https://www.google.com/search?q=Mountain {name}" 
        target="_blank">{name}</a></p>
    <p>Latitude: {lat}</p>
    <p>Longitude: {lon}</p>
    <p>Height: {elev} m</p>
    """
    fg.add_child(folium.Marker(
        location=coordinate,
        radius=6,
        # icon = icon,
        popup=html,
        fill_color=color_producer(elev),
        color= 'black',
        fill_opacity = 0.7
    ))

fg.add_child(folium.GeoJson(
    data=open(
        'world.json', 
        'r', 
        encoding='utf-8-sig').read()
    )
)

map.add_child(fg)
map.save("index.html");