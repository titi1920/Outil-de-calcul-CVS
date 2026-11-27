import streamlit as st
from calculs import calcul_hyd_autorite, calcul_hyd_debit_m3_h, calcul_deltapv100
from utils import widget_persistant, bouton_export_txt

st.header("Autorité d'une vanne")
nom_affaire = widget_persistant(st.text_input, "Nom du chantier :", "autorite_nom_affaire", "")
nom_reseau = widget_persistant(st.text_input, "Nom du réseau :", "autorite_nom_reseau", "")
st.subheader("Viser entre 0.3 et 0.7")

kvs = widget_persistant(st.number_input, "KVS (m³/h)", "autorite_kvs", 75.0, step=1.0, format="%.0f")
puissance_kw = widget_persistant(st.number_input, "Puissance (KW)", "autorite_puissance_kw", 232.0, step=0.001, format="%.3f")
t_depart = widget_persistant(st.number_input, "Température de départ (°C)", "autorite_t_depart", 35.0, step=0.1, format="%.1f")
t_retour = widget_persistant(st.number_input, "Température de retour (°C)", "autorite_t_retour", 30.0, step=0.1, format="%.1f")
deltap_debit_variable_mce = widget_persistant(st.number_input, "Delta p débit variable (mCE)", "autorite_deltap_debit_variable_mce", 8.0, step=0.1, format="%.1f")

if t_depart <= t_retour:
    st.error("La température de départ doit être supérieure à la température de retour")    
elif kvs <= 0:
    st.error("Le KVS doit être supérieur à 0 !")
elif deltap_debit_variable_mce <= 0:
    st.error("Le delta p doit être supérieur à 0 !")

else:
    debit_m3_h = calcul_hyd_debit_m3_h(puissance_kw, t_depart, t_retour)
    st.metric("Débit :", f"{debit_m3_h:.3f} m³/h")

    deltapv100 = calcul_deltapv100(debit_m3_h, kvs)
    st.metric("DeltaPv100 => (débit en m³/h / kvs)² x 100 :", f"{deltapv100:.2f} kPa")

    autorite = calcul_hyd_autorite(deltapv100, deltap_debit_variable_mce)
    st.metric("Autorité :", f"{autorite:.2f}")

bouton_export_txt(
    "Autorite_vanne", nom_affaire, nom_reseau,
    entrees={
        "KVS (m³/h)": kvs,
        "Puissance (kW)": f"{puissance_kw:.3f}",
        "Température de départ (°C)": f"{t_depart:.1f}",
        "Température de retour (°C)": f"{t_retour:.1f}",
        "Delta p débit variable (mCE)": f"{deltap_debit_variable_mce:.1f}",
    },
    resultats={
        "Débit (m³/h)": f"{debit_m3_h:.3f}",
        "DeltaPv100 (kPa)": f"{deltapv100:.2f}",
        "Autorité": f"{autorite:.2f}",
    },
)
