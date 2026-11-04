import streamlit as st
from calculs import calcul_hyd_dilatation, COEFFICIENTS_DILATATION

st.header("Dilatation linéique")
st.subheader("Trouver la dilatation de la conduite")

materiau = st.selectbox("Matériau :", list(COEFFICIENTS_DILATATION.keys()))

longueur = st.number_input("Longueur de la conduite (m)", value=25, key="longueur")
t_min = st.number_input("Température minimale de l'eau (°C)", value=10, key="t_min")
t_max = st.number_input("Température maximale de l'eau (°C)", value=50, key="t_max")

if t_max > t_min:
    dilatation = calcul_hyd_dilatation(materiau, longueur, t_max, t_min)
    st.metric("La dilatation de la conduite est de :", f"{dilatation:.1f} mm")
else:
    st.error("La température minimale doit être inférieure à la température maximale")
