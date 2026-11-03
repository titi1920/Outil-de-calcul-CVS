import streamlit as st

st.set_page_config(page_title="Outils CVS", page_icon="images/Logo_JM_V21.3.png")
st.logo("images/Logo_JM_V21.3.png")

pages = {
    "ACCUEIL 🏠": [
        st.Page("pages/accueil.py", title="- Accueil"),
    ],
    "CHAUFFAGE 🔥️": [
        st.Page("pages/chauffage_puissance.py", title="- Débit / Puissance / Delta t"),
        st.Page("pages/chauffage_dilatation.py", title="- Dilatation linéique"),
    ],
    "VENTILATION 𖣘": [
        st.Page("pages/ventilation_gaines.py", title="- Taille de gaines"),
        st.Page("pages/ventilation_grilles.py", title="- Taille de grilles"),
        st.Page("pages/ventilation_puissance_batterie_chaud_monobloc.py", title="- Puissance batterie de chaud"),
    ],
    "SANITAIRE 💧": [
        st.Page("pages/sanitaire_puissance_ecs.py", title="- Puissance groupe ECS"),
    ],
}

pg = st.navigation(pages)
pg.run()