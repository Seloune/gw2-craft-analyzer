#========================================
# Craft Analyzer Guild Wars 2
# api.py
# version 0.4
#========================================

import requests

def recuperer_objet(id_objet):
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















































