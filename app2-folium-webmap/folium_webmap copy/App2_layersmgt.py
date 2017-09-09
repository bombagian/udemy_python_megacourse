import folium
import pandas as pd


#CREATE MAP

def marker_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'


df=pd.read_csv('Volcanoes.txt')

lat=list(df['LAT'])
lng=list(df['LON'])
el=list(df['ELEV'])


map=folium.Map(location=[48, -120], zoom_start=4, tiles='Mapbox Bright') #create base map with initial location





fgp=folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('app2-webmapping/world.json','r',encoding='utf-8-sig'),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
                            else 'orange' if 10000000<= x['properties']['POP2005']< 20000000
                            else 'red'}))

fgv=folium.FeatureGroup(name='Volcanoes') #create feature group for Volcanoes - you can put things in it and handle them as a single layer. 

#add markers to the feature group
for lt,lg,el in zip(lat,lng,el):
    fgv.add_child(folium.CircleMarker([lt,lg],fill_color=marker_color(el),popup=str(el)+" m",radius=6, color='grey',fill_opacity=0.7))


#add reature group to map
map.add_child(fgp)
map.add_child(fgv)


map.add_child(folium.LayerControl()) #ADD LAYERS management in the map (NB: it has to be called after all the map.add_child methods)


map.save("map5.html") #save it as html

