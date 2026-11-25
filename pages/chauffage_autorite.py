import streamlit as st
from calculs import calcul_hyd_autorite

st.header("Autorité d'une vanne")
st.subheader("Viser entre 0.3 et 0.7")

kvs = st.number_input("KVS (m³/h)", value=75, key="kvs")
puissance_kw = st.number_input("Puissance (kW)", value=232, key="puissance_kw")
t_depart = st.number_input("Température de départ (°C)", value=35, key="t_depart")
t_retour = st.number_input("Température de retour (°C)", value=30, key="t_retour")
delta_p_debit_variable_mce = st.number_input("Delta p débit variable (mCE)", value=8, key="delta_p_debit_variable_mce")

if t_depart > t_retour:
    autorite = calcul_hyd_autorite(kvs, puissance_kw, t_depart, t_retour, delta_p_debit_variable_mce)
    st.metric("Autorité =", f"{autorite:.2f}")   
else:
    st.error("La température de départ doit être supérieure à la température de retour")

