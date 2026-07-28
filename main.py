#========================================
# Craft Analyzer Guild Wars 2
# main.py
# version 0.2
#========================================

from functions.api import recuperer_objet


def main():
    id_objet = input("Entrez l'ID d'un objet que vous souhaitez analyser : ")
    objet = recuperer_objet(id_objet)

    if objet is not None:
        print(f"{objet['name']}")
    else:
        print("objet introuvable ou erreur lors de la requête.")


if __name__ == "__main__":
    main()