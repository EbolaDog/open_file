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

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for shop_dish in dishes:
        if shop_dish in cook_book.keys():
            for cook_dish in cook_book[shop_dish]:
                person_quantity = int(cook_dish['quantity']) * person_count
                shop_list.update({cook_dish['ingredient_name']: {'measure': cook_dish['measure'], 'quantity': person_quantity}})
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))