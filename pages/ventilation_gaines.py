import streamlit as st
from calculs import calcul_ven_gaines_circulaire_vitesse
from calculs import calcul_ven_gaines_rectangulaire_vitesse
from utils import widget_persistant, bouton_export_txt

st.header("Dimensionnement des gaines")
nom_affaire = widget_persistant(st.text_input, "Nom du chantier :", "ventilation_gaines_nom_affaire", "")
nom_reseau = widget_persistant(st.text_input, "Nom du réseau :", "ventilation_gaines_nom_reseau", "")
st.subheader("Vistesses admissibles dans les gaines")
st.write("Jusqu'à 1'000m³/h => 3m/s")
st.write("Jusqu'à 2'000m³/h => 4m/s")
st.write("Jusqu'à 4'000m³/h => 5m/s")
st.write("Jusqu'à 10'000m³/h => 6m/s")
st.write("Depuis 10'000m³/h => 7m/s")
st.subheader("Gaines circulaires")

debit1 = widget_persistant(st.number_input, "Débit en m³/h", "ventilation_gaines_debit1", 84.0, format="%.0f")
diametre = widget_persistant(st.number_input, "Diamètre en mm", "ventilation_gaines_diametre", 100.0, format="%.0f")

if debit1 > 0:
    vitesse1 = calcul_ven_gaines_circulaire_vitesse(debit1, diametre)
    st.metric("vitesse =", f"{vitesse1:.2f} m/s")
else:
    st.error("le débit doit être supérieur à 0")
    
st.subheader("Gaines rectangulaires")

debit2 = widget_persistant(st.number_input, "Débit en m³/h", "ventilation_gaines_debit2", 107.0, format="%.0f")
largeur = widget_persistant(st.number_input, "largeur en mm", "ventilation_gaines_largeur", 100.0, format="%.0f")
hauteur = widget_persistant(st.number_input, "hauteur en mm", "ventilation_gaines_hauteur", 100.0, format="%.0f")

if debit2 > 0:
    vitesse2 = calcul_ven_gaines_rectangulaire_vitesse(debit2, largeur, hauteur)
    st.metric("vitesse =", f"{vitesse2:.2f} m/s")
else:
    st.error("le débit doit être supérieur à 0")
    
bouton_export_txt(
    "Tailles_de_gaines", nom_affaire, nom_reseau,
    sections=[
        (
            "Gaines circulaires",
            {
                "Débit (m³/h)": f"{debit1:.0f}",
                "Diamètre gaine (mm)": f"{diametre:.0f}",
            },
            {
                "La vitesse est de (m/s)": f"{vitesse1:.2f}" if vitesse1 is not None else "-",
            },
        ),
        (
            "Gaines quadratiques",
            {
                "Débit (l/h)": f"{debit2:.0f}",
                "Largeur gaine (mm)": f"{largeur:.0f}",
                "hauteur gaine (mm)": f"{hauteur:.0f}",
            },
            {
                "La vitesse est de (m/s)": f"{vitesse2:.2f}" if vitesse2 is not None else "-",
            },
        ),
    ],
)
