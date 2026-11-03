import streamlit as st
from calculs import calcul_ven_gaines_circulaire_vitesse
from calculs import calcul_ven_gaines_rectangulaire_vitesse

st.header("Dimensionnement des gaines")
st.subheader("Vistesses admissibles dans les gaines")
st.write("Jusqu'à 1'000m³/h => 3m/s")
st.write("Jusqu'à 2'000m³/h => 4m/s")
st.write("Jusqu'à 4'000m³/h => 5m/s")
st.write("Jusqu'à 10'000m³/h => 6m/s")
st.write("Depuis 10'000m³/h => 7m/s")
st.header("Gaines circulaires")

debit1 = st.number_input("Débit en m³/h", value=84, key="debit1")
diametre = st.number_input("Diamètre en mm", value=100, key="diametre")

if debit1 > 0:
    vitesse1 = calcul_ven_gaines_circulaire_vitesse(debit1, diametre)
    st.metric("vitesse =", f"{vitesse1:.2f} m/s")
else:
    st.error("le débit doit être supérieur à 0")
    
st.subheader("Gaines rectangulaires")

debit2 = st.number_input("Débit en m³/h", value=107, key="debit2")
largeur = st.number_input("largeur en mm", value=100, key="largeur")
hauteur = st.number_input("hauteur en mm", value=100, key="hauteur")

if debit2 > 0:
    vitesse2 = calcul_ven_gaines_rectangulaire_vitesse(debit2, largeur, hauteur)
    st.metric("vitesse =", f"{vitesse2:.2f} m/s")
else:
    st.error("le débit doit être supérieur à 0")
