import streamlit as st
from PIL import Image


st.title("TOUTOU")

image_upload = st.file_uploader("Choisir une image",type=['jpg','jpeg','png']
