import streamlit as st
from calculs import calcul_hyd_debit, calcul_hyd_puissance, calcul_hyd_delta_t
from utils import widget_persistant, bouton_export_txt

st.header("Débit / Puissance / Delta t")
nom_affaire = widget_persistant(st.text_input, "Nom du chantier :", "chauffage_puissance_nom_affaire", "")
nom_reseau = widget_persistant(st.text_input, "Nom du réseau :", "chauffage_puissance_nom_reseau", "")
st.subheader("Trouver le débit")

puissance_1 = widget_persistant(st.number_input, "Puissance (W)", "chauffage_puissance_puissance_1", 1500.0, format="%.0f")
t_depart_1 = widget_persistant(st.number_input, "Température de départ (°C)", "chauffage_puissance_t_depart_1", 35.0, format="%.1f")
t_retour_1 = widget_persistant(st.number_input, "Température de retour (°C)", "chauffage_puissance_t_retour_1", 28.0, format="%.1f")

debit_1 = None
if t_depart_1 > t_retour_1:
    debit_1 = calcul_hyd_debit(puissance_1, t_depart_1, t_retour_1)
    st.metric("Débit =", f"{debit_1:.0f} l/h")   
else:
    st.error("La température de départ doit être supérieure à la température de retour")

st.subheader("Trouver la puissance")

debit_2 = widget_persistant(st.number_input, "Débit (l/h)", "chauffage_puissance_debit_2", 184.0, format="%.0f")
t_depart_2 = widget_persistant(st.number_input, "Température de départ (°C)", "chauffage_puissance_t_depart_2", 35.0, format="%.1f")
t_retour_2 = widget_persistant(st.number_input, "Température de retour (°C)", "chauffage_puissance_t_retour_2", 28.0, format="%.1f")

puissance_2 = None
if t_depart_2 > t_retour_2:
    puissance_2 = calcul_hyd_puissance(debit_2, t_depart_2, t_retour_2)
    st.metric("Puissance =", f"{puissance_2:.0f} W")
else:
    st.error("La température de départ doit être supérieure à la température de retour")

st.subheader("Trouver le delta t")

puissance_3 = widget_persistant(st.number_input, "Puissance (W)", "chauffage_puissance_puissance_3", 1500.0, format="%.0f")
debit_3 = widget_persistant(st.number_input, "Débit (l/h)", "chauffage_puissance_debit_3",  184.0, format="%.0f")

delta_t = None
if debit_3 > 0:
    delta_t = calcul_hyd_delta_t(debit_3, puissance_3)
    st.metric("Delta t =", f"{delta_t:.1f} °K")
else:
    st.error("La puissance et le débit doit être supérieur à 0 !")

bouton_export_txt(
    "Debit_puissance_deltat", nom_affaire, nom_reseau,
    sections=[
        (
            "Trouver le débit",
            {
                "Puissance (W)": f"{puissance_1:.0f}",
                "Température départ (°C)": f"{t_depart_1:.1f}",
                "Température retour (°C)": f"{t_retour_1:.1f}",
            },
            {
                "Le débit est de (l/h)": f"{debit_1:.0f}" if debit_1 is not None else "-",
            },
        ),
        (
            "Trouver la puissance",
            {
                "Débit (l/h)": f"{debit_2:.0f}",
                "Température départ (°C)": f"{t_depart_2:.1f}",
                "Température retour (°C)": f"{t_retour_2:.1f}",
            },
            {
                "La puissance est de (W)": f"{puissance_2:.0f}" if puissance_2 is not None else "-",
            },
        ),
        (
            "Trouver le delta t",
            {
                "Puissance (W)": f"{puissance_3:.0f}",
                "Débit (l/h)": f"{debit_3:.0f}",
            },
            {
                "Le delta t est de (°K)": f"{delta_t:.1f}" if delta_t is not None else "-",
            },
        ),
    ],
)
