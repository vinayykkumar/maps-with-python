import folium
map3 = folium.Map(location= [15.582987, 73.757706], zoom_start= 20, tiles = 'Stamen Terrain')

folium.Marker(location=[15.582987, 73.757706], popup = 'I am lost', icon = folium.Icon(icon= 'cloud')).add_to(map3)

folium.Marker(location=[15.607220, 73.764229], popup= 'Bu i can see you', icon = folium.Icon(color= 'green')).add_to((map3))

print(map3.save('test3.html'))