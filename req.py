import requests
from pprint import pprint

def getIngredients(requestedDrink):
    ingredientsList = ""
    for index in range (1, 12):
        if (json_res["strIngredient"+index] == ""):
            return ingredientsList
        else: #Get this to list things as ing1, ing2, ing3, and ing4
            ingredientsList += json_res["strMeasure%s" % (index)] + " of " + \
            json_res["strIngredient%s" % (index)]
    pprint(ingredientsList)
    return ingredientsList
    
def listIngredients(requestedDrink):
    print("Here are the ingredients you need to make ", requestedDrink)
    instructions = json_res["strInstructions"]
    ingredients = getIngredients(requestedDrink)
    
def multipleDrinksFound(drinksArray):
    print("We found multiple drinks with that name. Here they are!")
    for drink in drinksArray:
        print(drink["strDrink"])
    specificDrink = raw_input("Which drink did you want to see?\n")
    if (specificDrink in drinksArray):
        print("SUCCESS")
        listIngredients(specificDrink)
    else:
        print("DRINK NOT IN ARRAY")




requestedDrink = raw_input("Hello, what drink you would like to get info for?\n")

requestedDrink.replace(" ", "_")
print(requestedDrink)
response = requests.get("http://www.thecocktaildb.com/api/json/v1/1/search.php?s=%s" % (requestedDrink))

json_res = response.json()
drinksArray = json_res["drinks"]
if (drinksArray == None):
    print("Sorry, but we couldn't find that drink")
elif len(drinksArray) > 1:
    multipleDrinksFound(drinksArray)
else:
    print(drinksArray[0])