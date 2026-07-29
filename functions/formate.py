#========================================
# Craft Analyzer Guild Wars 2
# formate.py
#========================================


def formater_prix(prix_cuivre):

    # Mémorise le signe avant de travailler sur une valeur positive
    signe = "-" if prix_cuivre < 0 else ""

    # abs() Renvoie la valeur absolue du montant
    prix_cuivre = abs(prix_cuivre)

    piece_or = prix_cuivre // 10000

    piece_argent = (prix_cuivre % 10000) // 100

    piece_cuivre = prix_cuivre % 100

    if piece_or == 0 and piece_argent > 0:
        monnaie_gw2 = f"{piece_argent} pa {piece_cuivre} pc"

    elif piece_or == 0 and piece_argent == 0:
        monnaie_gw2 = f"{piece_cuivre} pc"
        
    else:
        monnaie_gw2 = f"{piece_or} po {piece_argent} pa {piece_cuivre} pc"

    return signe + monnaie_gw2


def formater_pourcentage(valeur):
    return f"{valeur:.2f} %"


def formater_discipline(discipline):

    liste_disciplines_formatees = []

    traductions = {
    "Huntsman": "Chasseur",
    "Artificer": "Artificier",
    "Armorsmith": "Forgeron d'armures",
    "Weaponsmith": "Forgeron d'armes",
    "Jeweler": "Joailler",
    "Leatherworker": "Travailleur du cuir",
    "Tailor": "Tailleur",
    "Chef": "Chef"
}

    if isinstance(discipline, list):
        for discipline_api in discipline:
         liste_disciplines_formatees.append(traductions.get(discipline_api, discipline_api))
        return liste_disciplines_formatees
    
    else:
        return(traductions.get(discipline, discipline)) 































































