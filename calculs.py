c_eau = 4.186
f_eau = 0.86
f_air = 0.32
pi = 3.1416

def calcul_hyd_debit(puissance_w, t_depart, t_retour):
    """Retourne le débit en l/h."""
    delta_t = t_depart - t_retour
    return puissance_w * f_eau / delta_t
    
def calcul_hyd_puissance(debit_l_h, t_depart, t_retour):
    """Retourne la puissance en W."""
    delta_t = t_depart - t_retour
    return debit_l_h / f_eau * delta_t
    
def calcul_hyd_delta_t(debit_l_h, puissance_w):
    """Retourne le delta t en °K"""
    return puissance_w * f_eau / debit_l_h
    
COEFFICIENTS_DILATATION = {
    "Acier -> 0.0114 mm/m/k" : 0.0114,
    "Acier inox -> 0.0172 mm/m/k" : 0.0172,
    "Fonte -> 0.0100 mm/m/k" : 0.0100,
    "Cuivre -> 0.0162 mm/m/k" : 0.0162,
    "PVC -> 0.0800 mm/m/k" : 0.0800,
    "PE -> 0.2000 mm/m/k" : 0.2000,
}

def calcul_hyd_dilatation(materiau, longueur_m, t_max, t_min):
    """Retourne la dilatation en mm."""
    coefficient = COEFFICIENTS_DILATATION[materiau]
    return coefficient * longueur_m * (t_max - t_min)



def calcul_ven_gaines_circulaire_vitesse(debit_m3_h, diametre) :
    """Retourne la vitesse en m/s"""
    surface = pi * (diametre / 2000)**2
    return debit_m3_h / surface / 3600
    
def calcul_ven_gaines_rectangulaire_vitesse(debit_m3_h, largeur, hauteur):
    """Retourne la vitesse en m/s"""
    return debit_m3_h / ((largeur / 1000) * (hauteur / 1000)) / 3600
    
def calcul_ven_grilles_circulaire_vitesse(debit_m3_h, diametre, surface_libre) :
    """Retourne la vitesse en m/s"""
    surface = pi * (diametre / 2000)**2
    return debit_m3_h / (surface * (surface_libre / 100)) / 3600
    
def calcul_ven_grilles_rectangulaire_vitesse(debit_m3_h, largeur, hauteur, surface_libre):
    """Retourne la vitesse en m/s"""
    return debit_m3_h / (((largeur / 1000) * (hauteur / 1000))* (surface_libre / 100)) / 3600
    
def calcul_ven_puissance_batterie_chaud_monobloc(t1_air_neuf, t2_air_pulse, t3_air_extrait, rendement, debit):
    """Retourne la puissance de la batterie de chaud"""
    return debit * f_air * (t2_air_pulse - (t1_air_neuf + ((rendement / 100) * (t3_air_extrait - t1_air_neuf))))

def calcul_ven_debit_hydraulique_batterie_chaud_monobloc(q_batterie, t_depart, t_retour):
    """Retourne le débit hydraulique de la batterie de chaud"""
    return q_batterie * f_eau / (t_depart - t_retour)



def calcul_san_puissance_groupe_ecs (t_ef, t_ec, contenance, temps_chauffe):
    """Retourne la puissance du groupe chauffage ecs"""
    return (contenance * c_eau * (t_ec - t_ef))/(temps_chauffe * 60)
    
def calcul_san_debit_groupe_ecs_cote_chauffage (q_ecs, ch_depart, ch_retour):
    """Retourne le débit du groupe chauffage ecs"""
    return q_ecs * f_eau / (ch_depart - ch_retour)
    
def calcul_san_debit_groupe_ecs_cote_sanitaire (q_ecs, t_ec, t_ef):
    """Retourne le débit du groupe chauffage ecs"""
    return q_ecs * f_eau / (t_ec - t_ef)
