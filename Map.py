import folium
m=folium.Map(location=[45.5236, -123.6750])
folium.CircleMarker(
    location=[45.5215, -122.6261],
    radius=50,
    popup='Laurelhurst Park',
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
).add_to(m)
m.save('index.html')