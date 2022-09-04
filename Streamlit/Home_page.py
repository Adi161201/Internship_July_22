import streamlit as st 
import pandas as pd 

st.title("Pubs in United Kingdom")

#st.subheader("Information about pubs ")

info = st.sidebar.selectbox(
    "Statistical Data",
    ('Number of Pub\'s','Data_shape','Head', 'Tail', 'Unique Area\'s', 'Null values', 'Describe'))

df1=pd.read_csv('open_pubs.csv')
df2=pd.read_csv('df2.csv')
if info=='Number of Pub\'s':
    st.subheader("Total Number of Pubs ")
    st.markdown(f'**{df1.shape[0]}**  Pubs  in  **UK**')

elif info == 'Data_shape':
    st.subheader("Shape of data ")
    st.text('Number of rows: {}'.format(df1.shape[0]))
    st.text('Number of columns: {}'.format(df1.shape[1]))

elif info== 'Head':
    st.subheader("Top 5 rows of data ")
    st.dataframe(df1.head())

elif info == 'Tail':
    st.subheader("Last 5 rows of data ")
    st.dataframe(df1.tail())


elif info=='Unique Area\'s':
    st.subheader("Unique locations of pubs ")
    st.markdown(f'Total no of unique locations where pubs are present in UK is **{len(df2.local_authority.unique())}** ')

elif info == 'Null values':
    st.subheader("NULL values in data ")
    st.markdown('**We can see that there are no null values in the data**')
    st.table(df1.isna().sum())

elif info == 'Describe':
    st.subheader("Statistical information of data ")
    st.table(df1.describe())

