from glob import glob

# Создаёт новый файл с пометкой «Список контактов.», для распознавания
# в дальнейшем. Файлы создаются с именами в нижнем регистре.
# Возвращает имя вновь созданного файла:

def create_file():
    file_name = input('Введите имя файла: ')
    file_name = file_name.lower()
    if ('.txt') not in file_name:
        file_name = file_name + '.txt'
    is_file = glob(file_name)
    if file_name in is_file:
        print('\nТакой файл уже существует.\nДействие отменено.\n')
        return ''
    else:
        with open(file_name, 'w', encoding = 'UTF-8') as file1:
            string = 'Список контактов.\n\n'
            file1.write(string)
            print(f'Файл «{file_name}» создан.\n')
        return file_name


# Дописка в файл:

def write_file(file_name, text):
    with open(file_name, 'a', encoding = 'UTF-8') as file:
        file.write(text)


# Ищет файлы в текущей директории по заданному шаблону.
# Возвращает список найденных текстовых файлов, в которых имеется первая
# строка «Список контактов.»

def search_file(mask):
    list_files = []
    [list_files.append(file) for file in glob(mask)]

    # Проверка не через цикл for, поскольку при пустом
    # списке возможна ошибка «Out of range»:
    i = 0
    while i != len(list_files):
        with open(list_files[i], 'r', encoding = 'UTF-8') as file:
            if file.read(17) == 'Список контактов.':
                i += 1
            else:
                del list_files[i]
    
    return list_files

# Ищет в файле со списком контактов заданную запись.
# Возвращает список найденных контактов, или сообщение
# «Контакт ... не найден»:

def search_contact(file_name):
    with open(file_name, 'r', encoding = 'UTF-8') as file:
        contacts_list_for_search = file.read().rstrip().split('\n\n')
    del contacts_list_for_search[0]

    print('Искать контакт по:\n'
          '1. Фамилии\n'
          '2. Имени\n'
          '3. Отчеству\n'
          '4. Городу\n'
          '5. Номеру телефона\n')
    menu_item = int(input('Выберите нужное: '))

    while 5 < menu_item < 1:
        print('Ошибка ввода!')
        menu_item = input('Выберите один из пунктов: ')
    
    result_list = []
    serching_string = input('Введите данные для поиска: ')
    print()

    item = menu_item - 1

    for i in range(len(contacts_list_for_search)):
        contact_string = contacts_list_for_search[i].replace('г.', ' ').split()
        if serching_string in contact_string[item]:
            result_list.append(contacts_list_for_search[i])

    if len(result_list) == 0:
        result_list.append('Контакт «' + serching_string + '» не найден')

    return result_list

# Выводит пронумерованный список найденных контактов и
# возвращает его вместе с введённым номером контакта.
# В случае отсутствия искомого контакта, возвращает нули:

def search_by_number(which_file):
    desired_contact = search_contact(which_file)
    if 'Контакт' in ''.join(desired_contact):
        print(''.join(desired_contact) + '\n')

        return '0', '0'

    for i in range(len(desired_contact)):
        print(str(i + 1) + '. ' + ''.join(desired_contact[i]) + '\n')
    number = int(input('Укажите номер записи: '))

    while number > len(desired_contact) or number < 1 :
        print('Ошибка ввода.')
        number = int(input('Укажите номер записи: '))

    return desired_contact, number

# Копирует указанный контакт в другой файл.
# При необходимости создаёт новый файл:

def contact_for_copy(which_file):
    desired_contact, number = search_by_number(which_file)
    if desired_contact == '0':

        return '0'
    
    copied_contact = desired_contact[number - 1] + '\n\n'
    pattern = '*.txt'
    list_files = search_file(pattern)
    del list_files[list_files.index(which_file)]
    if len(list_files) == 0:
        print('Нет файлов для вставки. Требуется создать новый файл.')
        new_file = create_file()
        if new_file != '':
            write_file(new_file, copied_contact)

            return copied_contact

        else:

            return '0'
        
    else:
        other_file = input('Введите имя файла: ')
        list_files = search_file(other_file)
        
        if other_file == which_file:
            print('Невозможно скопировать контакт в один и тот же файл.')

            return '0'

        elif len(list_files) != 0:
            write_file(other_file, copied_contact)

            return copied_contact
        
        else:
            print(f'Файл «{other_file}» не найден.')

            return '0'


# Удаляет выбранный контакт из текущего файла, и
# вставляет в указанный файл:

def cut_contact(opened_file):
    desired_contact = contact_for_copy(opened_file)
    if desired_contact != '0':
        deleting(opened_file, desired_contact)

# Удаляет выбранный контакт из текущего файла:

def delete_contact(opened_file):
    desired_contact, number = search_by_number(opened_file)
    if desired_contact != '0':
        contact_to_delete = desired_contact[number - 1]
        deleting(opened_file, contact_to_delete)

# Общая функция для вырезки и удаления контакта.
# Перезаписывает текущий файл:

def deleting(prepared_file, deleted_contact):
    with open(prepared_file, 'r', encoding = 'UTF-8') as file:
        contacts_list_for_search = file.read().rstrip().split('\n\n')

    del contacts_list_for_search[0]

    del contacts_list_for_search[contacts_list_for_search.index(deleted_contact.rstrip())]
    text_to_write = '\n\n'.join(contacts_list_for_search) + '\n\n'

    with open(prepared_file, 'w', encoding = 'UTF-8') as file:
        file.write('Список контактов.\n\n')

    write_file(prepared_file, text_to_write)
    
# Тело программы:

command = ''
current_file = ''
while command != '7':
    print('\nМеню:\n'
        '1. Создать файл\n'
        '2. Открыть файл\n'
        '3. Вывести весь список\n'
        '4. Добавить контакт\n'
        '5. Найти контакт\n'
        '6. Править список\n'
        '7. Выход')
    print()
    command = input('Выберите пункт меню: ')

    while command not in ('1', '2', '3', '4', '5', '6', '7'):
        print('Ошибочный ввод!')
        command = input('Выберите пункт меню: ')
            
    match command:

        case '1':
            print()
            current_file = create_file()

        case '2':
            print()
            pattern = '*.txt'
            list_files = search_file(pattern)
            if len(list_files) != 0:
                print('Найденные файлы:\n' + '\n'.join(list_files) + '\n')
                pattern = input('Введите имя файла: ')
                if len(search_file(pattern)) != 0:
                    current_file = pattern
                    print(f'Файл «{current_file}» открыт.')
                else:
                    print(f'Файл «{pattern}» не найден.')
            else:
                print('Файлы с телефонной книгой не найдены.')
            
        case '3':
            print()
            if current_file != '':
                with open(current_file, 'r', encoding = 'UTF-8') as file:
                    print(file.read())
            else:
                print('Вы забыли указать файл.\n')

        case '4':
            print()
            if current_file != '':
                surname = input('Введите фамилию: ')
                name = input('Введите имя: ')
                patronymic = input('Введите отчество: ')
                city = input('Введите город: ')
                phonenumber = input('Введите номер телефона: ')
                line = f'{surname} {name} {patronymic}; г. {city}; {phonenumber}\n\n'
                write_file(current_file, line)
            else:
                print('Вы забыли указать файл.\n')

        case '5':
            print()
            if current_file != '':
                found_contacts = search_contact(current_file)
                print('\n\n'.join(found_contacts) + '\n')
            else:
                print('Вы забыли указать файл.\n')

        case '6':
            print()
            if current_file != '':
                print('\nДоступные действия:\n'
                    '1. Копировать\n'
                    '2. Вырезать\n'
                    '3. Удалить')
                action = input('Выберите действие: ')
                print()
                while action not in ('1', '2', '3'):
                    print('Ошибка ввода.')
                    action = input('Выберите действие: ')
                    print()

                match action:

                    case '1':
                        contact_for_copy(current_file)

                    case '2':
                        cut_contact(current_file)
                        
                    case '3':
                        delete_contact(current_file)

            else:
                print('Вы забыли указать файл.\n')

        case '7':
            print('\nВсего хорошего!\n')
