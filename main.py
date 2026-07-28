#========================================
# Craft Analyzer Guild Wars 2
# main.py
# version 0.3
#========================================

from functions.api import recuperer_objet, recuperer_prix

separateur = "--------------------------------------------------------------"


def main():
    print("")
    id_objet = input("Entrez l'ID d'un objet que vous souhaitez analyser : ")
    objet = recuperer_objet(id_objet)

    if objet is not None:
        print(separateur)
        print(objet["name"])

        objet_prix = recuperer_prix(id_objet)

        if objet_prix is not None:
            print(f"Prix d'achat : {objet_prix['buys']['unit_price']}")
            print(f"Prix de vente : {objet_prix['sells']['unit_price']}")
        else:
            print("Prix indisponible.")

        print(separateur)

    else:
        print("Objet introuvable ou erreur lors de la requête.")


if __name__ == "__main__":
    main()

print("")