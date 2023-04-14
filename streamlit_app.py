import streamlit as st
from PIL import Image
from rembg import remove
from io import BytesIO



st.title("Remover de BG")

image_upload = st.file_uploader("Choisir une image",type=['jpg','jpeg','png'])

def convert_image(image):
  buf = BytesIO()
  image.save'buf, format='PNG')
  byte_im = buf.getvalue()
  return byte_im

if image_upload:
  image = Image.open(image_upload)
  fixed = remove(image)
  downloadable_image = convert_image(fixed)
