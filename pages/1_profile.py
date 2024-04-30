import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Load latitude and longitude data from the CSV file
wmo_id = pd.read_csv(f'data/WMO_ID.csv')

# Create a Folium map centered at the mean latitude and longitude
center_lat = wmo_id['Lat'].mean()
center_lon = wmo_id['Lon'].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=5)

st.header("Indonesia Station",divider='grey')

# Iterate through each row in the DataFrame and add markers
for index, row in wmo_id.iterrows():
    folium.Marker(
        location=[row['Lat'], row['Lon']],
        popup=row['wmo_id'],
        tooltip=row['Stasiun']
    ).add_to(m)

# Render Folium map in Streamlit
st_folium(m, width=725, height=400)
