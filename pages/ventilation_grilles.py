import streamlit as st
from calculs import calcul_ven_grilles_circulaire_vitesse
from calculs import calcul_ven_grilles_rectangulaire_vitesse
from utils import widget_persistant, bouton_export_txt

st.header("Dimensionnement des grilles")
nom_affaire = widget_persistant(st.text_input, "Nom du chantier :", "ventilation_grilles_nom_affaire", "")
nom_reseau = widget_persistant(st.text_input, "Nom du réseau :", "ventilation_grilles_nom_reseau", "")
st.subheader("Grilles circulaires")

debit1 = widget_persistant(st.number_input, "Débit en m³/h", "ventilation_grilles_debit1", 84.0, format="%.0f")
diametre = widget_persistant(st.number_input, "Diamètre en mm", "ventilation_grilles_diametre", 100.0, format="%.0f")
surface_libre1 = widget_persistant(st.number_input, "Surface libre en %", "ventilation_grilles_surface_libre1", 60.0, format="%.0f")

if debit1 <= 0:
    st.error("Le débit doit être supérieur à 0 !")
elif surface_libre1 <= 0:
    st.error("La surface libre doit être supérieure à 0 !")
    
else:   
    vitesse1 = calcul_ven_grilles_circulaire_vitesse(debit1, diametre, surface_libre1)
    st.metric("vitesse =", f"{vitesse1:.2f} m/s")
    
st.subheader("Grilles rectangulaires")

debit2 = widget_persistant(st.number_input, "Débit en m³/h", "ventilation_grilles_debit2", 107.0, format="%.0f")
largeur = widget_persistant(st.number_input, "largeur en mm", "ventilation_grilles_largeur", 100.0, format="%.0f")
hauteur = widget_persistant(st.number_input, "hauteur en mm", "ventilation_grilles_hauteur", 100.0, format="%.0f")
surface_libre2 = widget_persistant(st.number_input, "Surface libre en %", "ventilation_grilles_surface_libre2", 60.0, format="%.0f")

if debit2 <= 0:
    st.error("Le débit doit être supérieur à 0 !")
elif surface_libre2 <= 0:
    st.error("La surface libre doit être supérieure à 0 !")

else:    
    vitesse2 = calcul_ven_grilles_rectangulaire_vitesse(debit2, largeur, hauteur, surface_libre2)
    st.metric("vitesse =", f"{vitesse2:.2f} m/s")

bouton_export_txt(
    "Tailles_de_grilles", nom_affaire, nom_reseau,
    sections=[
        (
            "Grilles circulaires",
            {
                "Débit (m³/h)": f"{debit1:.0f}",
                "Diamètre gaine (mm)": f"{diametre:.0f}",
                "Surface libre (%)": f"{surface_libre1:.0f}",
            },
            {
                "La vitesse est de (m/s)": f"{vitesse1:.2f}" if vitesse1 is not None else "-",
            },
        ),
        (
            "Grilles quadratiques",
            {
                "Débit (l/h)": f"{debit2:.0f}",
                "Largeur gaine (mm)": f"{largeur:.0f}",
                "hauteur gaine (mm)": f"{hauteur:.0f}",
                "Surface libre (%)": f"{surface_libre2:.0f}",
            },
            {
                "La vitesse est de (m/s)": f"{vitesse2:.2f}" if vitesse2 is not None else "-",
            },
        ),
    ],
)
