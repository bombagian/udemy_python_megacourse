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


#Add points
fg=folium.FeatureGroup(name='MyMap') #create feature group



#add markers to the feature group
for lt,lg,el in zip(lat,lng,el):
    #fg.add_child(folium.Marker(location=[lt,lg],popup=str(el), icon=folium.Icon(color=marker_color(el))))
    #fg.add_child(folium.RegularPolygonMarker([lt, lg],popup=str(el), fill_color=marker_color(el),number_of_sides=3,radius=10))
    fg.add_child(folium.CircleMarker([lt,lg],fill_color=marker_color(el),popup=str(el)+" m",radius=6, color='grey',fill_opacity=0.7))

#add reature group to map
map.add_child(fg)

map.save("map3.html") #save it as html

