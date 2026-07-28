#========================================
# Craft Analyzer Guild Wars 2
# formate.py
# version 0.4
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






























































