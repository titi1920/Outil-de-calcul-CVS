import streamlit as st
from calculs import calcul_hyd_debit, calcul_hyd_puissance, calcul_hyd_delta_t

st.header("Débit / Puissance / Delta t")
st.subheader("Trouver le débit")

puissance_1 = st.number_input("Puissance (W)", value=1500, key="puissance_1")
t_depart_1 = st.number_input("Température de départ (°C)", value=35.0, format="%.1f", key="t_depart_1")
t_retour_1 = st.number_input("Température de retour (°C)", value=28.0, format="%.1f", key="t_retour_1")

if t_depart_1 > t_retour_1:
    debit_1 = calcul_hyd_debit(puissance_1, t_depart_1, t_retour_1)
    st.metric("Débit =", f"{debit_1:.0f} l/h")   
else:
    st.error("La température de départ doit être supérieure à la température de retour")

st.subheader("Trouver la puissance")

debit_2 = st.number_input("Débit (l/h)", value=184, key="debit_2")
t_depart_2 = st.number_input("Température de départ (°C)", value=35.0, format="%.1f", key="t_depart_2")
t_retour_2 = st.number_input("Température de retour (°C)", value=28.0, format="%.1f", key="t_retour_2")

if t_depart_2 > t_retour_2:
    puissance_2 = calcul_hyd_puissance(debit_2, t_depart_2, t_retour_2)
    st.metric("Puissance =", f"{puissance_2:.0f} W")
else:
    st.error("La température de départ doit être supérieure à la température de retour")

st.subheader("Trouver le delta t")

puissance_3 = st.number_input("Puissance (W)", value=1500, key="puissance_3")
debit_3 = st.number_input("Débit (l/h)", value = 184, key="debit_3")

delta_t = calcul_hyd_delta_t(debit_3, puissance_3)
st.metric("Delta t =", f"{delta_t:.1f} °K")
