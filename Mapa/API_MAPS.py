api_key= 'AIzaSyCIUu5YFfu5A_nwFb_E4BkfhqM38OSzOUo'
import pandas as pd
import googlemaps

dx=pd.read_excel(r'C:\Users\Blogs\Desktop\SPACE_APPS\Apps_covid\Mapa/testando_denovo.xlsx')
paises=[]
aux=0
for i in (dx['Country/Region']):
    paises.append(i)
    aux+=1

cont=0
for j in range(0,aux):
    df = pd.DataFrame({'address':[paises[cont]]})
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
    cont+=1
