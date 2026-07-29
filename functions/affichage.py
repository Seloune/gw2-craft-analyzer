#========================================
# Craft Analyzer Guild Wars 2
# affichage.py
#========================================


from functions.formate import formater_discipline


def afficher_infos_recette(recette):

    print(f"Quantité produite : {recette['output_item_count']}")

    disciplines_formatees = formater_discipline(recette["disciplines"])
            
    print("Disciplines requises :")
            
    for discipline in disciplines_formatees:
        print(f"- {discipline} {recette['min_rating']}")


def afficher_ingredients(recette, ingredients):

    for ingredient_recette in recette["ingredients"]:
        for ingredient in ingredients:
            if (ingredient["id"] == ingredient_recette["item_id"]):
                print(f"{ingredient['name']} x {ingredient_recette['count']}")
