

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for recipes in file:
        number_of_cook = int(file.readline())
        cook_list = []
        for i in range(number_of_cook):
            name, quantity, measure = file.readline().strip().split(' | ')
            cook_list.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[recipes.strip()] = cook_list

# for key, value in cook_book.items():
#     print(f' \n{key}')
#     for key in value:
#         print(f'{key}')


def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for ingred in dishes:
        for ingr in cook_book[ingred]:
            name_ingr = ingr.pop('ingredient_name')
            ingr['quantity'] = int(ingr['quantity']) * int(person_count)
            if name_ingr in shopping_list:
                ingr['quantity'] += shopping_list[name_ingr]['quantity']
            shopping_list.update({name_ingr: ingr})
    return shopping_list


res = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
print(res)
