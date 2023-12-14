# Write your solution here
def search_by_name(recipes, word: str):
    recepies_dict = prepare_data(recipes)
    search_result = []
    for recipe in recepies_dict:
        if word.lower() in recipe["name"].lower():
            search_result.append(recipe["name"])
    return search_result

def search_by_time(filename: str, prep_time: int):
    recepies_dict = prepare_data(filename)
    search_result = []
    for recipe in recepies_dict:
        if int(recipe["minutes"]) <= prep_time:
            search_result.append(f"{recipe["name"]}, preparation time {recipe["minutes"]} min")
    return search_result

def search_by_ingredient(filename: str, ingredient: str):
    recepies_dict = prepare_data(filename)
    search_result = []
    for recipe in recepies_dict:
        if ingredient in recipe["ingredients"]:
            search_result.append(f"{recipe["name"]}, preparation time {recipe["minutes"]} min")
    return search_result

def prepare_data(recipes):
    with open(recipes) as recepies1:
        recepies_dict = []
        current_recipe = {}
        current_ingredients = []

        for line in recepies1:
            line = line.strip()

            if len(line) == 0:
                if current_recipe:
                    current_recipe['ingredients'] = current_ingredients
                    recepies_dict.append(current_recipe)
                    current_recipe = {}
                    current_ingredients = []
                continue

            if 'name' not in current_recipe:
                current_recipe['name'] = line
            elif 'minutes' not in current_recipe:
                current_recipe['minutes'] = line
            else:
                current_ingredients.append(line)

        if current_recipe:
            current_recipe['ingredients'] = current_ingredients
            recepies_dict.append(current_recipe)

        return recepies_dict

if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)