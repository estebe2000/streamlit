import streamlit as st
from PIL import Image


st.title("Remover de BG")

image_upload = st.file_uploader("Choisir une image",type=['jpg','jpeg','png'])

if image_upload:
  image = Image.open(image_upload)
