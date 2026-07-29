#========================================
# Craft Analyzer Guild Wars 2
# main.py
#========================================


from functions.api import(
    recuperer_objet, 
    recuperer_prix, 
    rechercher_recette,
    recuperer_recette
)

from functions.formate import formater_prix

from functions.affichage import afficher_infos_recette, afficher_ingredients

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

        recette_objet = rechercher_recette(objet["id"])

        if recette_objet is not None:
            if not recette_objet:
                print("Craftable : non")
                print(separateur)
        
            else:
                print("Craftable : oui")
                print(separateur)

                recette_id = recette_objet[0]
                recette = recuperer_recette(recette_id)
        
                if recette is not None:
                    afficher_infos_recette(recette)      
        
                    liste_ids_ingredients = []
        
                    for ingredient_recette in recette["ingredients"]:
                        liste_ids_ingredients.append(ingredient_recette["item_id"])
        
                    liste_ingredients = recuperer_objet(liste_ids_ingredients)

                    if liste_ingredients is not None:
        
                        afficher_ingredients(recette, liste_ingredients)

                    else:
                        print("Impossible de récupérer la liste des ingrédients.")

                else:
                    print("Recette non récupérée ou erreur lors de la requête.")
        
        else:
            print("Recette introuvable ou erreur lors de la requête.")

    else:
        print("Objet introuvable ou erreur lors de la requête.")    


if __name__ == "__main__":
    main()

print("")



























































































