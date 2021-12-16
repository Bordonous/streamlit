import pandas as pd
import folium
import streamlit as st
from IPython.display import display
from folium import plugins
from geopy import distance
import ipywidgets
import geopy.geocoders
from folium.plugins import Fullscreen, minimap
import os.path

st.set_page_config(layout="wide")
#ładowanie pliku z punktami turystycznymi
dir_name = os.path.abspath(os.path.dirname(__file__))
location = os.path.join(dir_name, 'bobrza1.csv')
bobrza_locations = pd.read_csv(location)
bobrza_locations = bobrza_locations[["nazwa_zasobu", "lat", "lon","icon","color","type"]]

def _max_width_():
    max_width_str = f"max-width: 1200px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )
st.header("Trasa rowerowa 'Mała pętla doliny bobrzy' oraz jej zasoby")


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color:     #87CEEB;">
  <a class="navbar-brand" href="#" target="_blank"><h5><b>Dolina Bobrzy</b></h5></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#"><h5><b>Trasa rowerowa </b></h5><span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#" target="_blank"><h5><b>Galeria</b></h5></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#" target="_blank"><h5><b>Punkty na trasie rowerowej</b></h5></a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


st.markdown(
    """
<style>

h5 { font-size: 20px;
     font-color: #d1ce24;
     color: white;
     text-shadow: 1px 1px black;
    }


.Widget>label {
    color: white;
    font-family: monospace;
    background-color: blue;
}
[class^="st-b"]  {
    color: white;
    font-family: Helvetica;
    background-color: #;
   margin-top: 5px;
}
.st-bb {
    background-color: transparent;
}
.st-at {
    background-color: #red;
}
footer {
    font-family: monospace;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color: #white;
    background-color: #87ceeb;
}
header .decoration {
    background-image: none;
}
.css-1d391kg {
    height: 95%;
}

</style>
""",
    unsafe_allow_html=True,
)




#ładowanie pliku z punktami, za pomocą których wyznaczona zostanie trasa
location2 = os.path.join(dir_name, 'route.csv')
route_locations=pd.read_csv(location2)
route_locations=route_locations[["lat","lon"]]


map = folium.Map(location=[bobrza_locations.lat.mean(), bobrza_locations.lon.mean()], zoom_start=12, control_scale=True, zoom_control=True, position="right")
_max_width_()

#mierzenie odleglosci recznie
measure_control = plugins.MeasureControl(position='topleft', 
                                         active_color='red', 
                                         completed_color='red', 
                                         primary_length_unit='kilometers')

map.add_child(measure_control)

#rysowanie na mapie
draw = plugins.Draw(export=False)
draw.add_to(map)


Fullscreen().add_to(map)

minimap = plugins.MiniMap(toggle_display=True)
map.add_child(minimap)


route_lats_longs=route_locations[["lat","lon"]]
folium.PolyLine(route_lats_longs).add_to(map)




choice = ['wszystkie zasoby','obiekt religijny', 'obiekt turystyczny','obiekt przyrodniczy','obiekt historyczny','atrakcja','gastronomia','punkt widokowy','sklep']
choice_selected = st.sidebar.radio("Wybierz typ zasobu, który Cie interesuje",choice)
if (choice_selected=='atrakcja'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='atrakcja'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)

elif (choice_selected=='obiekt religijny'):
    for index, location_info in bobrza_locations.iterrows():
        if(location_info["type"]=='obiekt_religijny'):
            folium.Marker([location_info["lat"], location_info["lon"]],tooltip="Kliknij, aby dowiedzieć się więcej", popup=location_info["nazwa_zasobu"],icon=folium.Icon(icon=location_info["icon"], prefix='fa', color=location_info["color"])).add_to(map)

elif(choice_selected=='wszystkie zasoby'):
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
            
    

        
footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #87ceeb;
color: #242424;
text-align: center;
height: 5%;
text-shadow: 1px 1px black
}
p{
    color: white;
    font-size: 16px;
    font-weight: bold;
}
</style>
<div class="footer">
<p>Maciej Wojtyna Copyright 2021 </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)        
        

    
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    




