import folium
from folium import plugins
import pandas as pd
import numpy as np

Biblioteca = pd.read_csv(r'C:\Users\User\Desktop\time_series_covid19_confirmed_global.csv')

coordenadas = []

for lati,lng in zip(Biblioteca.Lat,Biblioteca.Long):
    coordenadas.append([lati,lng])

Mapa = folium.Map(location=[33.0,65.0],zoom_start=5)

Mapa.add_child(plugins.HeatMap(coordenadas))

folium.Marker([33.0,65.0],popup='Afeganistão',tooltip='Click aqui',
                    icon=folium.Icon(color='green')).add_to(Mapa)

Mapa.add_child(folium.LatLngPopup())

draw = plugins.Draw(export=True,)
draw.add_to(Mapa)

folium.raster_layers.TileLayer('Open Street Map').add_to(Mapa)
folium.raster_layers.TileLayer('Stamen Terrain').add_to(Mapa)
folium.raster_layers.TileLayer('Stamen Toner').add_to(Mapa)
folium.raster_layers.TileLayer('Stamen watercolor').add_to(Mapa)
folium.raster_layers.TileLayer('CartoDB Positron').add_to(Mapa)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(Mapa)

folium.LayerControl().add_to(Mapa)

minimap=plugins.MiniMap(toggle_display = True)
Mapa.add_child(minimap)
plugins.ScrollZoomToggler().add_to(Mapa)
plugins.Fullscreen(position = 'topright').add_to(Mapa)

Mapa.save("Casos no mundo.html")