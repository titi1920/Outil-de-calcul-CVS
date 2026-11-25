import streamlit as st
from calculs import calcul_hyd_autorite, calcul_hyd_debit_m3_h, calcul_deltapv100

st.header("Autorité d'une vanne")
st.subheader("Viser entre 0.3 et 0.7")

kvs = st.number_input("KVS (m³/h)", value=75, key="kvs")
puissance_kw = st.number_input("Puissance (KW)", value=232, key="puissance_kw")
t_depart = st.number_input("Température de départ (°C)", value=35, key="t_depart")
t_retour = st.number_input("Température de retour (°C)", value=30, key="t_retour")
deltap_debit_variable_mce = st.number_input("Delta p débit variable (mCE)", value=8, key="deltap_debit_variable_mce")

if t_depart > t_retour:
    debit_m3_h = calcul_hyd_debit_m3_h(puissance_kw, t_depart, t_retour)
    st.metric("Débit :", f"{debit_m3_h:.3f} m³/h")

    deltapv100 = calcul_deltapv100(debit_m3_h, kvs)
    st.metric("DeltaPv100 :", f"{deltapv100:.2f} kPa")
    
    autorite = calcul_hyd_autorite(deltapv100, deltap_debit_variable_mce)
    st.metric("Autorité :", f"{autorite:.2f}")

else:
    st.error("La température de départ doit être supérieure à la température de retour")
