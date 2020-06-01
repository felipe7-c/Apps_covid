# Código desenvolvido para o desafio Nasa Space App pela equipe #430
# Este código solicita sua localização( cidade, país, local específico) e retorna a latitude e longitude

api_key= 'AIzaSyCIUu5YFfu5A_nwFb_E4BkfhqM38OSzOUo'

import pandas as pd
import googlemaps

local_input = input('Digite sua localização (Cidade e Estado):')# pode inserir neste local qualquer informação
df = pd.DataFrame({                                             # sobre o local que deseja, podendo utilizar até código postal                    
   'address':[local_input]})

gmaps_key = googlemaps.Client(key= 'AIzaSyCIUu5YFfu5A_nwFb_E4BkfhqM38OSzOUo')
df['Lat'] = None
df['Lon'] = None
for i in range(len(df)):
    geocode_result = gmaps_key.geocode(df.loc[i,'address'])
    try:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        df.loc[i,'Lat'] = lat
        df.loc[i,'Lon'] = lng
    except:
        lat = None
        lng = None
print(df)