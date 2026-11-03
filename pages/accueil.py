import streamlit as st

st.markdown("<h1 style='text-align: center;'>Outils de calculs CVS</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Choisis un calcul dans le menu de gauche.</h3>", unsafe_allow_html=True)

# 3 colonnes ([1, 1, 1]) = 3 colonnes de même tailles, ([2, 1, 2]) colonne du milieu 2x plus petite
col1, col2, col3 =st.columns([1, 1, 1])
with col2:
   st.image("images/Logo_JM_V21.3.png", width=250)