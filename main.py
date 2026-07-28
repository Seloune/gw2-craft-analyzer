#========================================
# Craft Analyzer Guild Wars 2
# main.py
# version 0.4
#========================================

from functions.api import recuperer_objet, recuperer_prix

from functions.formate import formater_prix

separateur = "--------------------------------------------------------------"


def main():
    print("")
    id_objet = input("Entrez l'ID d'un objet que vous souhaitez analyser : ")
    objet = recuperer_objet(id_objet)

    if objet is not None:
        print(separateur)
        print(f"Nom de l'objet : {objet['name']}")

        objet_prix = recuperer_prix(id_objet)

        if objet_prix is not None:
            objet_prix_achat = objet_prix['buys']['unit_price']
            objet_prix_vente = objet_prix['sells']['unit_price']

            print(f"Prix d'achat   : {formater_prix(objet_prix_achat)}")
            print(f"Prix de vente  : {formater_prix(objet_prix_vente)}")

        else:
            print("Prix indisponible.")

        print(separateur)

    else:
        print("Objet introuvable ou erreur lors de la requête.")


if __name__ == "__main__":
    main()

print("")

























































































