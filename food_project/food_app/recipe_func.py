
def recipe_func(ingredients_list):
    recipes = {
        "wrap": {"Apples", "chicken", "carrot", "tomato", "turkey", "lettuce", "lentil"},
        "salad": {"lettuce", "tomato", "spinach", "onion", "walnut", "lentil"},
        "cake": {"flour", "milk", "egg", "butter", "carrot"},
        "casserole": {"cheese", "nutmeg", "chicken", "butter", "milk", "onion"},
    }

    available_recipes = []
    for recipe, ingredients in recipes.items():
        if all(ingredient in ingredients_list for ingredient in ingredients):
            available_recipes.append(recipe)

