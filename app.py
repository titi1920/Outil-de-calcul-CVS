import streamlit as st

st.set_page_config(page_title="Outils CVS", page_icon="images/Logo_JM_V21.3.png")
st.logo("images/Logo_JM_V21.3.png")

pages = {
    "Accueil 🏠": [
        st.Page("pages/accueil.py", title="-Accueil"),
    ],
    "Chauffage 🔥️": [
        st.Page("pages/chauffage_puissance.py", title="-Débit / Puissance / Delta t"),
        st.Page("pages/chauffage_dilatation.py", title="-Dilatation linéique"),
    ],
    "Ventilation 𖣘": [
        st.Page("pages/ventilation_gaines.py", title="-Gaines : dimensionnement"),
        st.Page("pages/ventilation_grilles.py", title="-Grilles : dimensionnement"),
        st.Page("pages/ventilation_puissance_batterie_chaud_monobloc.py", title="-Batterie de chaud : dimensionnement"),
    ],
    "Sanitaire 💧": [
        st.Page("pages/sanitaire_puissance_ecs.py", title="-Puissance groupe ECS"),
    ],
}

pg = st.navigation(pages)
pg.run()