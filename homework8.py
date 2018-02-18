def create_cook_book():
    with open("cook_book.txt") as f:
        cook_book = {}
        dishes_list = []
        ingridients_list = []
        number_of_ingridients_list = []
        ingridients_list_spl = []
        ingridients_list_dict = []
        ingridients = {}
        for line in f:
            dishes_list.append(line.strip())
            number_of_ingridients = f.readline().strip()
    
            for i in number_of_ingridients:
                number = int(i)
            number_of_ingridients_list.append(number)
            j = 1
            while j <= number:
                j += 1
                ingridients_list.append(f.readline().strip())
            f.readline()
        for params in ingridients_list:
            ingridients_list_spl.append(params.split(' | '))
        i = 0
        while i < sum(number_of_ingridients_list):  
            ingridients = {'ingridient_name': ingridients_list_spl[i][0],\
                      'quantity': int(ingridients_list_spl[i][1]),\
                      'measure': ingridients_list_spl[i][2]}
            ingridients_list_dict.append(ingridients)
            i += 1
        start = 0
        end = 0
        iteration = 0
        for dish in dishes_list:
            end += number_of_ingridients_list[iteration]
            cook_book[dish] = ingridients_list_dict[start:end]
            start += number_of_ingridients_list[iteration]
            iteration += 1
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in create_cook_book()[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=\
                    new_shop_list_item['quantity']
    return shop_list
    
def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],\
              shop_list_item['measure']))
def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
            .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)
    
create_shop_list()
    
    
