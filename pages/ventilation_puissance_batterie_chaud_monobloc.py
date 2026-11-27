import streamlit as st
from calculs import calcul_ven_puissance_batterie_chaud_monobloc
from calculs import calcul_ven_debit_hydraulique_batterie_chaud_monobloc
from utils import widget_persistant, bouton_export_txt

st.header("Dimensionnement batterie de chaud")
nom_affaire = widget_persistant(st.text_input, "Nom du chantier :", "ventilation_puissance_nom_affaire", "")
nom_reseau = widget_persistant(st.text_input, "Nom du réseau :", "ventilation_puissance_nom_reseau", "")
st.subheader("Trouver la puissance et le débit")

t1_air_neuf = widget_persistant(st.number_input, "Température air neuf (°C) :", "ventilation_puissance_t1_air_neuf", -10.0, format="%.1f")
t2_air_pulse = widget_persistant(st.number_input, "Température air pulsé (°C) :", "ventilation_puissance_t2_air_pulse", 21.0, format="%.1f")
t3_air_repris = widget_persistant(st.number_input, "Température air repris (°C) :", "ventilation_puissance_t3_air_repris", 21.0, format="%.1f")
rendement = widget_persistant(st.number_input, "Rendement récupérateur (%) :", "ventilation_puissance_rendement", 80.0, format="%.1f")
debit_v = widget_persistant(st.number_input, "Débit du monobloc (m³/h) :", "ventilation_puissance_debit", 3270.0, format="%.0f")
tch_depart = widget_persistant(st.number_input, "Température départ chauffage (°C) :", "ventilation_puissance_tch_depart", 23.0, format="%.1f")
tch_retour = widget_persistant(st.number_input, "Température retour chauffage (°C) :", "ventilation_puissance_tch_retour", 20.4, format="%.1f")

if debit_v > 0:
    puissance = calcul_ven_puissance_batterie_chaud_monobloc(t1_air_neuf, t2_air_pulse, t3_air_repris, rendement, debit_v)
    st.metric("La puissance chaud de la batterie est de :", f"{puissance:.0f} W")
else:
    st.error("Le débit doit être supérieur à 0.")
    
if tch_depart > tch_retour:
    debit_c = calcul_ven_debit_hydraulique_batterie_chaud_monobloc(puissance, tch_depart, tch_retour)
    st.metric("Le débit côté chauffage est de :", f"{debit_c:.0f} l/h")
    
else:
    st.error("La température de départ doit être supérieure à la température de retour.")
    
bouton_export_txt(
    "Puissance_batterie_chaud_monobloc", nom_affaire, nom_reseau,
    entrees={
        "Température air neuf (°C)": f"{t1_air_neuf:.1f}",
        "Température air pulsé (°C)": f"{t2_air_pulse:.1f}",
        "Température air repris (°C)": f"{t3_air_repris:.1f}",
        "Rendement récupérateur (%)": f"{rendement:.1f}",
        "Débit monobloc (m³/h)": f"{debit_v:.0f}",
        "Température départ chauffage (°C)": f"{tch_depart:.1f}",
        "Température retour chauffage (°C)": f"{tch_retour:.1f}",
    },
    resultats={
        "Puissance batterie (W)": f"{puissance:.0f}",
        "Débit chauffage (l/h)": f"{debit_c:.0f}",
    },
)
