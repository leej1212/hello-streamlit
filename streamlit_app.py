import streamlit as st

x = st.slider('Select a value')
st.write(x, 'is a squared of', x * x)