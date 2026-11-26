import streamlit as st
from calculs import calcul_hyd_debit, calcul_hyd_puissance, calcul_hyd_delta_t
from utils import widget_persistant

st.header("Débit / Puissance / Delta t")
nom_affaire = widget_persistant(st.text_input, "Nom du chantier :", "chauffage_puissance_nom_affaire", "")
nom_reseau = widget_persistant(st.text_input, "Nom du réseau :", "chauffage_puissance_nom_reseau", "")
st.subheader("Trouver le débit")

puissance_1 = widget_persistant(st.number_input, "Puissance (W)", "chauffage_puissance_puissance_1", 1500.0, format="%.0f")
t_depart_1 = widget_persistant(st.number_input, "Température de départ (°C)", "chauffage_puissance_t_depart_1", 35.0, format="%.1f")
t_retour_1 = widget_persistant(st.number_input, "Température de retour (°C)", "chauffage_puissance_t_retour_1", 28.0, format="%.1f")

if t_depart_1 > t_retour_1:
    debit_1 = calcul_hyd_debit(puissance_1, t_depart_1, t_retour_1)
    st.metric("Débit =", f"{debit_1:.0f} l/h")   
else:
    st.error("La température de départ doit être supérieure à la température de retour")

st.subheader("Trouver la puissance")

debit_2 = widget_persistant(st.number_input, "Débit (l/h)", "chauffage_puissance_debit_2", 184.0, format="%.0f")
t_depart_2 = widget_persistant(st.number_input, "Température de départ (°C)", "chauffage_puissance_t_depart_2", 35.0, format="%.1f")
t_retour_2 = widget_persistant(st.number_input, "Température de retour (°C)", "chauffage_puissance_t_retour_2", 28.0, format="%.1f")

if t_depart_2 > t_retour_2:
    puissance_2 = calcul_hyd_puissance(debit_2, t_depart_2, t_retour_2)
    st.metric("Puissance =", f"{puissance_2:.0f} W")
else:
    st.error("La température de départ doit être supérieure à la température de retour")

st.subheader("Trouver le delta t")

puissance_3 = widget_persistant(st.number_input, "Puissance (W)", "chauffage_puissance_puissance_3", 1500.0, format="%.0f")
debit_3 = widget_persistant(st.number_input, "Débit (l/h)", "chauffage_puissance_debit_3",  184.0, format="%.0f")

if debit_3 > 0:
    delta_t = calcul_hyd_delta_t(debit_3, puissance_3)
    st.metric("Delta t =", f"{delta_t:.1f} °K")
else:
    st.error("La puissance et le débit doit être supérieur à 0 !")
