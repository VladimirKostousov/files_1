

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

for key, value in cook_book.items():
    print(f' \n{key}')
    for key in value:
        print(f'{key}')