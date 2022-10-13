cook_book = {}

with open('files/recipes.txt', 'rt', encoding='utf8') as file:
    for i in file:
        dish = i.strip()
        ingredients = []
        ingredients_list = file.readline()
        for i in range(int(ingredients_list)):
            ingred = file.readline()
            ingredient_name, quantity, measure = ingred.strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure})
        book = file.readline()
        cook_book.update({dish: ingredients})
print(cook_book)