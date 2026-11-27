import streamlit as st
from calculs import calcul_san_puissance_groupe_ecs
from calculs import calcul_san_debit_groupe_ecs_cote_chauffage
from calculs import calcul_san_debit_groupe_ecs_cote_sanitaire
from utils import widget_persistant, bouton_export_txt

st.header("Calcul puissance groupe boiler")
nom_affaire = widget_persistant(st.text_input, "Nom du chantier :", "sanitaire_puissance_nom_affaire", "")
nom_reseau = widget_persistant(st.text_input, "Nom du réseau :", "sanitaire_puissance_nom_reseau", "")
st.subheader("Trouver la puissance et les débits")

t_ef = widget_persistant(st.number_input, "Température eau froide (°C)", "sanitaire_puissance_t_ef", 10.0, format="%.0f")
t_ec = widget_persistant(st.number_input, "Température eau chaude (°C)", "sanitaire_puissance_t_ec", 60.0, format="%.0f")
ch_depart = widget_persistant(st.number_input, "Température départ chauffage (°C)", "sanitaire_puissance_ch_depart", 75.0, format="%.0f")
ch_retour = widget_persistant(st.number_input, "Température retour chauffage (°C)", "sanitaire_puissance_ch_retour", 40.0, format="%.0f")
contenance = widget_persistant(st.number_input, "Contenance du boiler (litres)", "sanitaire_puissance_contenance", 300.0, format="%.0f")
temps_de_chauffe = widget_persistant(st.number_input, "Temps de chauffe (minutes)", "sanitaire_puissance_temps_de_chauffe", 90.0, format="%.0f")

if t_ec <= t_ef:
    st.error("La température de l'eau chaude doit être supérieure à la température de l'eau froide !")
elif ch_depart <= ch_retour:
    st.error("La température de départ doit être supérieure à la température de retour !")
elif contenance <= 0:
    st.error("La contenance doit être supérieure à 0 !")
elif temps_de_chauffe <= 0:
    st.error("Le temps de chauffe doit être supérieur à 0 !")

else:
    puissance = calcul_san_puissance_groupe_ecs(t_ef, t_ec, contenance, temps_de_chauffe)
    st.metric("La puissance nécessaire est de :", f"{puissance:.3f} KW")

    debit1 = calcul_san_debit_groupe_ecs_cote_chauffage(puissance, ch_depart, ch_retour)
    st.metric("Débit côté chauffage :", f"{debit1:.3f} m³/h")
    
    debit2 = calcul_san_debit_groupe_ecs_cote_sanitaire(puissance, t_ec, t_ef)
    st.metric("Débit côté sanitaire :", f"{debit2:.3f} m³/h")

bouton_export_txt(
    "Puissance_groupe_boiler", nom_affaire, nom_reseau,
    entrees={
        "Température eau froide (°C)": f"{t_ef:.0f}",
        "Température eau chaude (°C)": f"{t_ec:.0f}",
        "Température départ chauffage (°C)": f"{ch_depart:.0f}",
        "Température retour chauffage (°C)": f"{ch_retour:.0f}",
        "Contenance boiler (litres)": f"{contenance:.0f}",
        "Temps de chauffe (min)": f"{temps_de_chauffe:.0f}",
    },
    resultats={
        "Puissance (kW)": f"{puissance:.3f}",
        "Débit chauffage (m³/h)": f"{debit1:.3f}",
        "Débit sanitaire (m³/h)": f"{debit2:.3f}",
    },
)
