import folium


#CREATE MAP

map=folium.Map(location=[51.490772, 0.038219], zoom_start=6, tiles='Mapbox Bright') #create base map with initial location

#ADD POINTS

fg=folium.FeatureGroup(name='MyMap') #create feature group

#add markers to the feature group
fg.add_child(folium.Marker(location=[51.5,0.04],popup="Hello!", icon=folium.Icon(color="red"))) 

#add reature group to map
map.add_child(fg)

map.save("map1.html") #save it as html


