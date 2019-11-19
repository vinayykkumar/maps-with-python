import folium
import pandas as pd

map4 = folium.Map(location=[15.607220, 73.764229], zoom_start=5, tiles='Stamen Terrain')
df = pd.read_csv('volcano.csv')

def color(elev):
    if elev in range(0,1000):
        col = 'green'
    elif elev in range(1001, 1999):
        col = 'blue'
    elif elev in range(2000,2999):
        col = 'red'
    else:
        col = 'black'
    return col
for lat, lan, name, elev in zip(df['Lat'], df['Lon'], df['name'], df['Elevation']):
    folium.Marker(location=[lat, lan], popup='name', icon=folium.Icon(color = color(elev), icon='cloud')).add_to(map4)

print(map4.save('test4.html'))