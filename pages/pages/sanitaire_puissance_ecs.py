import streamlit as st
from calculs import calcul_san_puissance_groupe_ecs
from calculs import calcul_san_debit_groupe_ecs_cote_chauffage
from calculs import calcul_san_debit_groupe_ecs_cote_sanitaire

st.title("Calcul puissance groupe boiler")

t_ef = st.number_input("Température eau froide (°C)", value=10, key="t_ef")
t_ec = st.number_input("Température eau chaude (°C)", value=60, key="t_ec")
ch_depart = st.number_input("Température départ chauffage (°C)", value=75, key="ch_depart")
ch_retour = st.number_input("Température retour chauffage (°C)", value=40, key="ch_retour")
contenance = st.number_input("Contenance du boiler (litres)", value=300, key="contenance")
temps_de_chauffe = st.number_input("Temps de chauffe (minutes)", value=90, key="temps_de_chauffe")

if t_ec > t_ef:
    puissance = calcul_san_puissance_groupe_ecs(t_ef, t_ec, contenance, temps_de_chauffe)
    st.metric("La puissance nécessaire est de :", f"{puissance:.3f} KW")
else:
    st.error("La température de l'eau chaude doit être supérieure à la température de l'eau froide")
    
if ch_depart > ch_retour:
    debit1 = calcul_san_debit_groupe_ecs_cote_chauffage(puissance, ch_depart, ch_retour)
    st.metric("Débit côté chauffage :", f"{debit1:.3f} m³/h")
else:
    st.error("La température de départ doit être supérieure à la température de retour")
    
debit2 = calcul_san_debit_groupe_ecs_cote_sanitaire(puissance, t_ec, t_ef)
st.metric("Débit côté sanitaire :", f"{debit2:.3f} m³/h")
