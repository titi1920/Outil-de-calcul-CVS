import streamlit as st
from calculs import calcul_hyd_dilatation, COEFFICIENTS_DILATATION
from utils import widget_persistant, bouton_export_txt

st.header("Dilatation linéique")
nom_affaire = widget_persistant(st.text_input, "Nom du chantier :", "chauffage_dilatation_nom_affaire", "")
nom_reseau = widget_persistant(st.text_input, "Nom du réseau :", "chauffage_dilatation_nom_reseau", "")
st.subheader("Trouver la dilatation de la conduite")

materiau = widget_persistant(st.selectbox, "Matériau", "chauffage_dilatation_materiau", list(COEFFICIENTS_DILATATION.keys())[0], options=list(COEFFICIENTS_DILATATION.keys()))
longueur = widget_persistant(st.number_input, "Longueur de la conduite (m)", "chauffage_dilatation_longueur", 25.0, format="%.0f")
t_min = widget_persistant(st.number_input, "Température minimale de l'eau (°C)", "chauffage_dilatation_t_min", 10.0, format="%.0f")
t_max = widget_persistant(st.number_input, "Température maximale de l'eau (°C)", "chauffage_dilatation_t_max", 50.0, format="%.0f")

if t_max > t_min:
    dilatation = calcul_hyd_dilatation(materiau, longueur, t_max, t_min)
    st.metric("La dilatation de la conduite est de :", f"{dilatation:.1f} mm")
else:
    st.error("La température minimale doit être inférieure à la température maximale")
    
bouton_export_txt(
    "Dilatation_lineique", nom_affaire, nom_reseau,
    entrees={
        "Matériau": materiau,
        "Longueur (m)": f"{longueur:.0f}",
        "Température minimale (°C)": f"{t_min:.0f}",
        "Température maximale (°C)": f"{t_max:.0f}",
    },
    resultats={
        "La dilatation de la conduite est de (mm)": f"{dilatation:.1f}",
    },
)
