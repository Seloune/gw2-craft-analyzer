#========================================
# Craft Analyzer Guild Wars 2
# main.py
#========================================

import json

from functions.api import(
    recuperer_objet, 
    recuperer_prix, 
    rechercher_recette,
    recuperer_recette
)

from functions.formate import formater_prix, formater_discipline

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

        recette_objet = rechercher_recette(objet['id'])

        if recette_objet is not None:
            if not recette_objet:
                print("Craftable : non")
                print(separateur)
            else:
                print("Craftable : oui")
                print(separateur)

                # Récupération de la 1ère recette trouvée
                recette_id = recette_objet[0]

                recette = recuperer_recette(recette_id)

#            if recette is not None:
#                # Recette test : 19783 - Inscription sur bois vert vitale
#                print(recette)
#                print(f"Quantité produite : {recette['output_item_count']}")
#                print(f"Discipline (niveau) : {formater_discipline(recette['disciplines'][0])} ({recette['min_rating']})")
#            else:
#                print("Recette non récupérée ou erreur lors de la requête.")

            if recette is not None:
                # Recette test : 19783 - Inscription sur bois vert vitale
                print(f"Quantité produite : {recette['output_item_count']}")
                #print(f"Discipline (niveau) : {formater_discipline(recette['disciplines'][0])} ({recette['min_rating']})")
                
                disciplines_formatees = formater_discipline(recette['disciplines'])

                print("Disciplines requises : ")
                for discipline in disciplines_formatees:
                    print(f"- {discipline} {recette['min_rating']}")
                
            else:
                print("Recette non récupérée ou erreur lors de la requête.")

        else:
            print("Recette introuvable ou erreur lors de la requête.")
            
    else:
        print("Objet introuvable ou erreur lors de la requête.")    


if __name__ == "__main__":
    main()

print("")



























































































