import streamlit as st
from calculs import calcul_ven_puissance_batterie_chaud_monobloc
from calculs import calcul_ven_debit_hydraulique_batterie_chaud_monobloc

st.header("Dimensionnement batterie de chaud")

t1_air_neuf = st.number_input("Température air neuf (°C) :", value=-10.0, format="%.1f", key="t1_air_neuf")
t2_air_pulse = st.number_input("Température air pulsé (°C) :", value=21.0, format="%.1f", key="t2_air_pulse")
t3_air_repris = st.number_input("Température air repris (°C) :", value=21.0, format="%.1f", key="t3_air_repris")
rendement = st.number_input("Rendement récupérateur (%) :", value=80.0, format="%.1f", key="rendement")
debit_v = st.number_input("Débit du monobloc (m³/h) :", value=3270, key="debit")
tch_depart = st.number_input("Température départ chauffage (°C) :", value=23.0, format="%.1f", key="tch_depart")
tch_retour = st.number_input("Température retour chauffage (°C) :", value=20.4, format="%.1f", key="tch_retour")

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
