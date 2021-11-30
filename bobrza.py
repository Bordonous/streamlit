import pandas as pd
import folium
import streamlit as st
from IPython.display import display
from folium import plugins
from geopy import distance
import ipywidgets
import geopy.geocoders
from folium.plugins import Fullscreen, minimap
from pathlib import Path

st.set_page_config(layout="centered", initial_sidebar_state="expanded")
#ładowanie pliku z punktami turystycznymi
location=Path(__file__).parents[1] / 'D:/streamlit/bobrza1.csv'
bobrza_locations = pd.read_csv(location)
bobrza_locations = bobrza_locations[["nazwa_zasobu", "lat", "lon","icon","color","type"]]


#ładowanie pliku z punktami, za pomocą których wyznaczona zostanie trasa
location2='D:/streamlit/route.csv'
route_locations=pd.read_csv(location2)
route_locations=route_locations[["lat","lon"]]

json1=f"D:/streamlit/bobrza.geojson"

map = folium.Map(location=[bobrza_locations.lat.mean(), bobrza_locations.lon.mean()], zoom_start=12, control_scale=True, zoom_control=True)



# for index, location_info in bobrza_locations.iterrows():
#     folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],
#     	icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)

#st.map(data=bobrza_locations)





#mierzenie odleglosci recznie
measure_control = plugins.MeasureControl(position='topleft', 
                                         active_color='red', 
                                         completed_color='red', 
                                         primary_length_unit='kilometers')

map.add_child(measure_control)

#rysowanie na mapie
draw = plugins.Draw(export=False)
draw.add_to(map)

#mierzenie odleglosci w lini prostej automatycznie

# start_location = st.text_input('value')
# route_stop_widget = ipywidgets.Text(value='', placeholder='address', description='stop:')

# def get_distance(start_address, stop_address):
    
#     # string addresses to location information
#     start_location = geocoder.osm(start_address)
#     stop_location = geocoder.osm(stop_address)
    
#     # pull out latitude and longitude from location information
#     start_latlng = [start_location.lat, start_location.lng]
#     stop_latlng = [stop_location.lat, stop_location.lng]
    
#     # calculate distance from start point to stop point using latitudes and longitudes
#     distance = geopy.distance.distance(start_latlng, stop_latlng).miles
#     print(f'distance: {distance:.2f} miles')
    
#     # map
#     distance_path = [(start_latlng), (stop_latlng)]
#     map_distance = folium.Map(location=[38, -98], zoom_start=4)
#     plugins.AntPath(distance_path).add_to(map_distance)
#     display(map_distance)

# ipywidgets.interact_manual(get_distance, start_address=route_start_widget, stop_address=route_stop_widget)
Fullscreen().add_to(map)

minimap = plugins.MiniMap(toggle_display=True)
map.add_child(minimap)


route_lats_longs=route_locations[["lat","lon"]]
folium.PolyLine(route_lats_longs).add_to(map)
#folium.GeoJson(json1, name='typ').add_to(map)
#folium.LayerControl().add_to(map)
st.write("Trasa rowerowa 'Mała pętla doliny bobrzy' oraz jej zasoby")



choice = ['wszystkie punkty','obiekt religijny', 'obiekt turystyczny','obiekt przyrodniczy','obiekt historyczny','atrakcja','gastronomia','punkt widokowy','sklep']
choice_selected = st.selectbox("Wybierz typ zasobu, który Cie interesuje",choice)
if (choice_selected=='atrakcja'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='atrakcja'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)

elif (choice_selected=='obiekt religijny'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='obiekt_religijny'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)

elif(choice_selected=='wszystkie punkty'):
    for index, location_info in bobrza_locations.iterrows():
        folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)

elif (choice_selected=='obiekt historyczny'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='obiekt_historyczny'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)

elif (choice_selected=='obiekt noclegowy'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='obiekt_noclegowy'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)

elif (choice_selected=='obiekt przyrodniczy'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='obiekt_przyrodniczy'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)

elif (choice_selected=='obiekt turystyczny'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='obiekt_turystyczny'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)       

elif (choice_selected=='sklep'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='sklep'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)
        
   
elif (choice_selected=='punkt widokowy'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='punkt_widokowy'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)
          
elif (choice_selected=='gastronomia'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='gastronomia'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)
        

map
            
    

        
        
        

    

    




