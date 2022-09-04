import streamlit as st
import pandas as pd
import numpy as np

st.subheader('Nearest five Pubs based on user enter Latitude and longitude')
df4 = pd.read_csv("D:\\internship_july_22\\Streamlit\\updated_pubdata.csv")

#st.markdown('Nearest five Pubs based on user enter Latitude and longitude')

lat = st.sidebar.number_input('The latitude of place')
lon = st.sidebar.number_input('The longitude of place')
button = st.button("Search")
df_new = df4[['latitude', 'longitude']]
new_points = np.array([lat, lon])

# Calculate distance between new_points and all points in df_new using Euclidean distance 
distances = np.sqrt(np.sum((new_points - df_new)**2, axis = 1))


# sort the array using arg partition and keep only 5 elements
n = 5
min_indices = np.argpartition(distances,n-1)[:n]
if button:
    st.map(df4.iloc[min_indices])
    st.text("The location corresponding to below nearest distances : ")
    st.dataframe(df4.iloc[min_indices])
    