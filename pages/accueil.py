import streamlit as st
import base64
from pathlib import Path

st.markdown("<h1 style='text-align: center;'>Outils de calculs CVS</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Choisis un calcul dans le menu de gauche.</h3>", unsafe_allow_html=True)

DOSSIER = Path(__file__).parent.parent  # dossier où se trouve accueil.py

def image_base64(chemin):
    return base64.b64encode(Path(chemin).read_bytes()).decode()

img = image_base64(DOSSIER / "images" / "Logo_JM_V21.3.png")

st.markdown(
    f'<div style="text-align:center;"><img src="data:image/png;base64,{img}" style="max-width:250px; width:100%; height:auto;"></div>',
    unsafe_allow_html=True,
)
