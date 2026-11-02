import streamlit as st
from calculs import calcul_ven_puissance_batterie_chaud_monobloc

st.title("Dimensionnement batterie de chaud")

t1_air_neuf = st.number_input("Température air neuf (°C) :", value=-10, key="t1_air_neuf")
t2_air_pulse = st.number_input("Température air pulsé (°C) :", value=21, key="t2_air_pulse")
t3_air_repris = st.number_input("Température air repris (°C) :", value=21, key="t3_air_repris")
rendement = st.number_input("Rendement récupérateur (%) :", value=80, key="rendement")
debit = st.number_input("Débit du monobloc (m³/h) :", value=3270, key="debit")

if debit > 0:
    puissance = calcul_ven_puissance_batterie_chaud_monobloc(t1_air_neuf, t2_air_pulse, t3_air_repris, rendement, debit)
    st.metric("La puissance chaud de la batterie est de :", f"{puissance:.0f} W")
else:
    st.error("Le débit doit être supérieur à 0")