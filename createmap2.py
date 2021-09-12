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

for lat, lon, elev, name in zip(lattiude, longitude, elevation, name):  

    if elev < 1000:
        color = "green"
    elif ((elev > 1000) and (elev < 2000)):
        color = "blue"
    elif ((elev > 2000) and (elev < 2500)):
        color = "darkpurple"
    elif elev > 3000:
        color = "beige"
    else:
        color = "red"  

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
        popup=html,
        icon=folium.Icon(color)
    ))

map.add_child(fg)

map.add_child
map.save("index.html");