#========================================
# Craft Analyzer Guild Wars 2
# api.py
# version 0.1
#========================================

import requests

def recuperer_objet(id_objet):
    url = f"https://api.guildwars2.com/v2/items/{id_objet}?lang=fr"
    reponse = requests.get(url)

    if reponse.status_code == 200:
        return reponse.json()

    return None