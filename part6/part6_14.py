"""
    This is the recipes megaquestion on part 6
"""

def flatten_recipe (filepath : str) -> list :

    recipes_data = "recipes.txt"
    
    with open(recipes_data) as recipes :
        content = recipes.read()
        recipe_list = content.split("\n\n")       
       
    print ("Recipes list ::", recipe_list)
    true_recipe_list = []    

    i = 0
    size = len(recipe_list)

    while i < size :
        recipe = recipe_list[i].split("\n")        
        true_recipe_list.append(recipe)
        i += 1
        
    print ("True recipe list ::", true_recipe_list)

    return true_recipe_list


def search_by_name (filepath : str, key : str) -> list :

    true_recipe_list = flatten_recipe (filepath)
    ret_list = []

    for list in true_recipe_list :
        #print(list)
        if key in str.lower(list[0]) :
            ret_list.append(list[0])
    
    return ret_list


def search_by_time (filepath : str, key : int) -> list :

    true_recipe_list = flatten_recipe (filepath)
    ret_list = []

    for list in true_recipe_list :
        #print(f"list :: {list}") 
               
        if key >= int(list[1]) :            
            ret_list.append([list[0], list[1]])
    
    return ret_list

def search_by_ingredient (filepath : str, key : str) -> list :

    true_recipe_list = flatten_recipe (filepath)
    ret_list = []

    for list in true_recipe_list :
        #print(f"list :: {list}") 
               
        # if key in list[1:] :            
        #     ret_list.append([list[0], list[1]])

        for obj in list[1:] :
            if key.lower() == obj.lower() :
                ret_list.append([list[0], list[1]])
    
    return ret_list


if __name__ == "__main__" :    

    ## found_recipes = search_by_name("recipes1.txt", "cake")

    # for recipe in found_recipes:
    #     print(recipe)

    
    # found_recipes = search_by_time("recipes1.txt", 20)

    # for recipe in found_recipes:
    #     print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)


