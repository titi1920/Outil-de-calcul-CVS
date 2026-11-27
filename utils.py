import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

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

def bouton_export_txt(titre_fichier, nom_affaire, nom_reseau,
                      entrees=None, resultats=None, sections=None):
    """
    Soit entrees + resultats (1 seul calcul),
    soit sections = [(titre, entrees, resultats), ...] (plusieurs calculs).
    """
    maintenant = datetime.now(ZoneInfo("Europe/Paris"))
    horodatage = maintenant.strftime("%Y%m%d_%H%M%S")

    # Si un seul calcul, on le met dans une liste de sections
    if sections is None:
        sections = [(None, entrees or {}, resultats or {})]

    texte = f"Chantier : {nom_affaire}\n"
    texte += f"Réseau : {nom_reseau}\n"
    texte += f"Date : {maintenant.strftime('%d/%m/%Y %H:%M')}\n"

    for titre, ent, res in sections:
        texte += "\n"
        if titre:
            texte += f"=== {titre} ===\n"
        texte += "DONNÉES\n"
        texte += "\n".join(f"{k} : {v}" for k, v in ent.items())
        texte += "\n\nRÉSULTATS\n"
        texte += "\n".join(f"{k} : {v}" for k, v in res.items())
        texte += "\n"

    nom_propre = (nom_affaire or "sans_nom").replace(" ", "_")
    nom_fichier = f"{titre_fichier}_{nom_propre}_{horodatage}.txt"

    st.download_button(
        "📥 Exporter en TXT",
        data=texte.encode("utf-8-sig"),
        file_name=nom_fichier,
        mime="text/plain",
    )
