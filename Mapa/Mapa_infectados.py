import pandas as pd
import folium
import numpy
from folium.plugins import HeatMap
df=pd.read_excel(r"C:\Users\Blogs\Desktop\SPACE_APPS\Apps_covid\Mapa/new_teste.xlsx",error_bad_lines=False)
print(df)
lat=df["lat"].to_list()
long=df["lon"].to_list()
#infectados=df["Infectados"].to_list()
quant=len(long)
quant=int(quant)
quant_final=quant
mp=folium.Map(location=[33,65],zoom_start=3,tiles="Stamen Terrain")
coordenada=[]
for i in range(quant_final):
    coordenada.append([float(lat[i]),float(long[i])])#,int(infectados[i])
    #folium.CircleMarker(location=[float(lat[i]),float(long[i])],radius=10,control_scale=True).add_to(mp)

#novo=folium.CircleMarker(location=[-14.235, -51.9253],radius=10,control_scale=True).add_to(mp)
#novo_denovo=folium.CircleMarker(location=[370902,-957129],radius=10).add_to(mp)

HeatMap(coordenada).add_to(mp)
mp.save('finish.html')



