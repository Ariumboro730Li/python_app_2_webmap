import folium
import pandas
import random

df = pandas.read_csv("Volcanoes.txt")

dfone = df.loc[1]
map = folium.Map(location = [dfone.LAT, dfone.LON], 
    zoom_start=6, 
    tiles="Stamen Terrain"
)
 
fg = folium.FeatureGroup(name="My Map")

# lengthtxt = len(df)
# for item in range(0, lengthtxt):
#     lat = df.loc[item].LAT
#     lon = df.loc[item].LON
#     coordinate = [lat, lon]
#     fg.add_child(folium.Marker(
#         location=coordinate,
#         popup= f"Latitude =  {lat}, Longitude = {lon}",
#         icon=folium.Icon(color="red")
#     ))

lattiude = list(df.LAT)
longitude = list(df.LON)
elevation = list(df.ELEV)
name = list(df.NAME)

color = ["red", "blue", "green", "orange", "purple", "darkpurple"]
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
        # popup= f"{lat}, {lon}, {elev} m",
        popup=html,
        icon=folium.Icon(color=random.choice(color))
    ))

map.add_child(fg)

map.add_child
map.save("index.html");