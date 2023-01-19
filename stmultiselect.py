import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'What are your favorite colors',
    ['Snowflake Blue', 'Mid Blue', 'Midnight'],
    ['Star Blue', 'Valencia Orange', 'Purple Moon' 'First Light' 'Windy City']) 

st.write('You selected:', options) 
