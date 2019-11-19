import folium
print(dir(folium))

map = folium.Map(location=[17.385044, 78.486671], zoom_start = 7)
print(map)

print(dir(folium.Map))
print(map.save('test.html'))

map2 = folium.Map(location=[17.385044, 78.486671], zoom_start= 15, tiles = 'Stamen terrain')
print(map2)
print(map2.save('test2.html'))