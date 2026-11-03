import streamlit as st
from calculs import calcul_ven_grilles_circulaire_vitesse
from calculs import calcul_ven_grilles_rectangulaire_vitesse

st.header("Dimensionnement des grilles")
st.subheader("Grilles circulaires")

debit1 = st.number_input("Débit en m³/h", value=84, key="debit1")
diametre = st.number_input("Diamètre en mm", value=100, key="diametre")
surface_libre1 = st.number_input("Surface libre en %", value=60, key="surface_libre1")

if debit1 > 0:
    vitesse1 = calcul_ven_grilles_circulaire_vitesse(debit1, diametre, surface_libre1)
    st.metric("vitesse =", f"{vitesse1:.2f} m/s")
else:
    st.error("le débit doit être supérieur à 0")
    
st.subheader("Grilles rectangulaires")

debit2 = st.number_input("Débit en m³/h", value=107, key="debit2")
largeur = st.number_input("largeur en mm", value=100, key="largeur")
hauteur = st.number_input("hauteur en mm", value=100, key="hauteur")
surface_libre2 = st.number_input("Surface libre en %", value=60, key="surface_libre2")

if debit2 > 0:
    vitesse2 = calcul_ven_grilles_rectangulaire_vitesse(debit2, largeur, hauteur, surface_libre2)
    st.metric("vitesse =", f"{vitesse2:.2f} m/s")
else:
    st.error("le débit doit être supérieur à 0")
