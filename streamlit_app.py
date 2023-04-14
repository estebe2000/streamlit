# documentation : https://docs.streamlit.io/library/api-reference
# Importation de bibliothèques nécessaires
import streamlit as st  # Pour la création de l'application web
from PIL import Image, ImageOps  # Pour la manipulation d'images
from rembg import remove  # Pour la suppression de l'arrière-plan des images
from io import BytesIO  # Pour la gestion de fichiers binaires

# Configuration de la page
st.set_page_config(page_title="remover de bg",page_icon=":skull:",layout='wide')

# Titre de l'application
st.write("# Remover de BG")

# Description de l'application
st.write("Upload une image pour effectuer différentes transformations")

# Zone latérale pour le choix de l'option
option = st.sidebar.selectbox('Choisir une option',('Détourage', 'Filtre en noir et blanc', 'Inversion de couleurs'))

# Zone latérale pour l'upload de l'image
st.sidebar.write("## Uploader")

# Division de l'écran en deux colonnes
col1,col2 = st.columns(2)

# Fonction pour convertir l'image en format binaire
def convert_image(image):
  buf = BytesIO()
  image.save(buf, format='PNG')
  byte_im = buf.getvalue()
  return byte_im

# Fonction pour effectuer les différentes transformations sur l'image
def transform_image(image, option, color=None):
  image = Image.open(image)
  col1.write("Image originale")  # Affichage du titre "Image originale" dans la première colonne
  col1.image(image)  # Affichage de l'image originale dans la première colonne
  if option == 'Détourage':  # Si l'option choisie est le détourage
    fixed = remove(image)  # Suppression de l'arrière-plan de l'image
    col2.write("Image détourée")  # Affichage du titre "Image détourée" dans la deuxième colonne
    col2.image(fixed)  # Affichage de l'image détourée dans la deuxième colonne
    st.write("\n")  # Ajout d'une ligne vide
    col2.download_button("Télécharger l'image détourée", convert_image(fixed),'removebg.png','image/png')  # Bouton pour télécharger l'image détourée
  elif option == 'Filtre en noir et blanc':  # Si l'option choisie est le filtre en noir et blanc
    fixed = image.convert('L')  # Conversion de l'image en noir et blanc
    col2.write("Image en noir et blanc")  # Affichage du titre "Image en noir et blanc" dans la deuxième colonne
    col2.image(fixed)  # Affichage de l'image en noir et blanc dans la deuxième colonne
    st.write("\n")  # Ajout d'une ligne vide
    col2.download_button("Télécharger l'image en noir et blanc", convert_image(fixed),'bw.png','image/png')  # Bouton pour télécharger l'image en noir et blanc
  elif option == 'Inversion de couleurs':  # Si l'option choisie est l'inversion de couleurs
    fixed = ImageOps.invert(image)  # Inversion des couleurs de l'image
    col2.write("Image avec les couleurs inversées")  # Affichage du titre "Image avec les couleurs inversées" dans la deuxième colonne
    col2.image(fixed)  # Affichage de l'image avec les couleurs inversées dans la deuxième colonne
    st.write("\n")  # Ajout d'une ligne vide
    col2.download_button("Télécharger l'image avec les couleurs inversées", convert_image(fixed),'invert.png','image/png')  # Bouton pour télécharger l'image avec les couleurs inversées
  return

# Upload de l'image et appel de la fonction pour effectuer les transformations
uploaded_file = st.sidebar.file_uploader("Choisir une image", type=["jpg","jpeg","png"])
if uploaded_file is not None:
  transform_image(uploaded_file, option)
else:
  st.sidebar.write("Veuillez uploader une image")

