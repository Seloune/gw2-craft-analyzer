#========================================
# Craft Analyzer Guild Wars 2
# affichage.py
#========================================


from functions.formate import(
    formater_discipline, 
    formater_prix
)


def afficher_infos_recette(recette):

    print(f"Quantité produite : {recette['output_item_count']}")

    disciplines_formatees = formater_discipline(recette["disciplines"])
            
    print("Disciplines requises :")
            
    for discipline in disciplines_formatees:
        print(f"- {discipline} {recette['min_rating']}")



def afficher_ingredients(recette, ingredients, prix):

    for ingredient_recette in recette["ingredients"]:
        for ingredient in ingredients:
            if (ingredient["id"] == ingredient_recette["item_id"]):

                cout_formate = "prix indisponible"
                prix_total_formate = "prix indisponible"

                for cout in prix:
                    if cout['id'] == ingredient['id']:
                        cout_formate = formater_prix(cout['sells']['unit_price'])
                        prix_total_formate = formater_prix(cout['sells']['unit_price'] * ingredient_recette['count'])

                if ingredient_recette['count'] == 1:
                    print(f"{ingredient['name']} = {prix_total_formate}")

                else:
                    print(f"{ingredient['name']} x {ingredient_recette['count']} ({cout_formate} / unité) = {prix_total_formate}")
