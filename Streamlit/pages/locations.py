import streamlit as st 
import pandas as pd 
import numpy as np 

df4 = pd.read_csv("D:\\internship_july_22\\Streamlit\\updated_pubdata.csv")


st.title('UK MAP PUB Locations')


local = df4.local_authority.unique()
st.sidebar.markdown("Choose Area")
option = st.sidebar.selectbox('',local)


'You Selected : ' ,option



btn_clk = st.button('Search')
if btn_clk==True:
    new_df = df4[df4['local_authority']==option]
    new_df=new_df[['latitude','longitude']]
    st.success('All the pubs in the area being selected are displayed .')
    st.map(new_df)