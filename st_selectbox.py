import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Snowflake Blue', 'Mid Blue', 'Midnight'))

st.write('Your favorite color is ', option)
