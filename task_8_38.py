
#### * Задача 38: 
#     Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n', '').split(sep=', ')
            data_array.append(item)
    return data_array


def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')


def add_item(filename, lastname='', firstname='', secondname='', phone=''):
    data_array = read_file(filename)
    max_id = 0
    for i in range(1, len(data_array)):
        if max_id < int(data_array[i][0]):
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    write_file(filename, data_array)


def show_all_items(filename):
    data_array = read_file(filename)
    for i in range(1, len(data_array)):
        print("ID:", data_array[i][0], "  Фамилия:", data_array[i][1], "  Имя:",
              data_array[i][2], "  Отчество:", data_array[i][3], "  Телефон:", data_array[i][4])


def change_item(filename):
    data_array = read_file(filename)
    data_item_change = input('Введите данные для поиска: ')
    data_item_change = data_item_change.lower()
    for i in range(1, len(data_array)):
        j = 0
        while j < len(data_array[i]):
            if data_item_change in data_array[i][j].lower():
                print("ID:", data_array[i][0], "  Фамилия:", data_array[i][1], "  Имя:",
                      data_array[i][2], "  Отчество:", data_array[i][3], "  Телефон:", data_array[i][4])
                j = len(data_array[i])
            j += 1
    id_item_change = input('Введите "ID" изменяемой записи: ')
    data_item_change1 = input('Введите данные которые хотите изменить: ').lower()
    data_item_change2 = input(
        'Введите данные которые нужно сохранить взамен изменяемых: ')
    for line in range(1, len(data_array)):
        if id_item_change == data_array[line][0]:
            k = 1
            while k < len(data_array[line]):
                if data_item_change1 == data_array[line][k].lower():
                    data_array[line][k] = data_item_change2
                    k = len(data_array[line])
                elif k == len(data_array[line]) - 1:
                    print(f'>>> Таких "данных" не существует в "ID" {id_item_change}!')
                k += 1
            break
        elif line == len(data_array) - 1:
            print('>>> Такого "ID" не существует!!!')    
    write_file(filename, data_array)


def delete_item(filename):
    data_array = read_file(filename)
    data_item_delete = input('Введите данные для поиска: ')
    data_item_delete = data_item_delete.lower()
    for i in range(1, len(data_array)):
        j = 0
        while j < len(data_array[i]):
            if data_item_delete in data_array[i][j].lower():
                print("ID:", data_array[i][0], "  Фамилия:", data_array[i][1], "  Имя:",
                      data_array[i][2], "  Отчество:", data_array[i][3], "  Телефон:", data_array[i][4])
                j = len(data_array[i])
            j += 1
    id_item_delete = input('Введите "ID" удаляемой записи: ')
    line = 1
    flag = True
    while flag:
        if id_item_delete == data_array[line][0]:
            del data_array[line]
            flag = False
        elif line == len(data_array):
            print('>>> Такого "ID" не существует!!!')
            flag = False
        else:
            line += 1
    write_file(filename, data_array)


def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input())
    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2:
        add_item(filename)
    elif user_operation == 3:
        change_item(filename)
    elif user_operation == 4:
        delete_item(filename)


filename = 'file.txt'
menu()
