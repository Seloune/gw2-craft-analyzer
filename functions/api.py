#========================================
# Craft Analyzer Guild Wars 2
# api.py
#========================================

import requests


def recuperer_objet(id_objet):

    if isinstance(id_objet, list):
        liste_ids_objets = ",".join(str(identifiant) for identifiant in id_objet)
        url = f"https://api.guildwars2.com/v2/items?ids={liste_ids_objets}&lang=fr"

    else:
        url = f"https://api.guildwars2.com/v2/items/{id_objet}?lang=fr"
    reponse = requests.get(url, timeout=5)

    if reponse.status_code == 200:
        return reponse.json()

    return None


def recuperer_prix(id_objet):
    url = f"https://api.guildwars2.com/v2/commerce/prices/{id_objet}"
    reponse = requests.get(url, timeout=5)

    if reponse.status_code == 200:
        return reponse.json()

    return None


def rechercher_recette(id_objet):
    url = f"https://api.guildwars2.com/v2/recipes/search?output={id_objet}"
    reponse = requests.get(url, timeout=5)

    if reponse.status_code == 200:
        return reponse.json()

    return None


def recuperer_recette(id_recette):
    url = f"https://api.guildwars2.com/v2/recipes/{id_recette}?lang=fr"
    reponse = requests.get(url, timeout=5)

    if reponse.status_code == 200:
        return reponse.json()

    return None


















































