import streamlit as st
from PIL import Image


st.set_page_config(page_title='Attendance System', layout='wide')


st.markdown("# Attendance System using Face Recognition")


# Add welcome message
st.write("<h2 style='font-size: 2.5rem;'>Welcome to your company! This is the Attendance System using Face Recognition.</h2>", unsafe_allow_html=True)

with st.spinner("Loading Models and Connecting to Redis db ..."):
    import face_rec
    
st.success('Model loaded successfully')
st.success('Redis db successfully connected')
