import math


def cakes(recipe, available):
    min_number_of_cakes = math.inf
    for rec_ingredient in recipe:
        if rec_ingredient in available:
            count_ingredients = math.floor(available[rec_ingredient] / recipe[rec_ingredient])
            if count_ingredients < min_number_of_cakes:
                min_number_of_cakes = count_ingredients
        else:
            return 0

    return min_number_of_cakes


if __name__ == "__main__":
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe, available))