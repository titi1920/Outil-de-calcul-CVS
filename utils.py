import streamlit as st

def _sauve(cle):
    """Recopie la valeur du widget dans une clé de sauvegarde permanente."""
    st.session_state["_save_" + cle] = st.session_state[cle]

def init_valeur(cle, defaut):
    """À appeler avant le widget : restaure la valeur sauvegardée (ou la valeur par défaut)."""
    if cle not in st.session_state:
        st.session_state[cle] = st.session_state.get("_save_" + cle, defaut)

def widget_persistant(widget, label, cle, defaut, **kwargs):
    """Crée un widget dont la valeur survit au changement de page."""
    init_valeur(cle, defaut)
    return widget(label, key=cle, on_change=_sauve, args=(cle,), **kwargs)