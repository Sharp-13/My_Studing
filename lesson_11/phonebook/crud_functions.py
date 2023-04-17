import json

def create_number():

    phone_number = number_entry()

    with open('phonebook.json', 'r') as phonebook_file:
        phonebook_container = json.load(phonebook_file)

    if is_number_in_phonebook(phonebook_container, phone_number):
        print('Такий номер вже є у базі')
        return
    else:
        phonebook_container[phone_number] = add_number_data()

    with open('phonebook.json', 'w') as phonebook_file:
        json.dump(phonebook_container, phonebook_file)
    print('Запис додано успішно!')


def search_number():
    with open('phonebook.json', 'r') as phonebook_file:
        phonebook_container = json.load(phonebook_file)

    COICE_SEARCH_METHOD = '''Будь ласка, виберіть метод пошуку:
    1. Пошук за номером телефону
    2. Пошук за іменем
    3. Пошук за прізвищем
    4. Пошук за повним іменем
    5. Пошук по місту/країні
    ------------------------
    0. Повернутись до головного меню
    '''
    search_method = input(COICE_SEARCH_METHOD)
    search_method_dict = {
        '1': find_by_number,
        '2': find_by_name,
        '3': find_by_surname,
        '4': find_by_fullname,
        '5': find_by_city_state
    }

    if int(search_method) in range(1, 6):
        search_method_dict[search_method](phonebook_container)
    elif search_method == '0':
        return
    else:
        print('Такого методу не існує')



def update_number():
    phone_number = number_entry()
    with open('phonebook.json', 'r') as phonebook_file:
        phonebook_container = json.load(phonebook_file)

    if not is_number_in_phonebook(phonebook_container, phone_number):
        print('Такого номеру немає у базі')
        return
    else:
        current_number_data = phonebook_container.pop(phone_number)
    CHOICE_FIELD_TEXT = '''Будь ласка, вкажіть поле, в яке Ви хотіли б внести зміни:
    1. Ім'я
    2. Прізвище
    3. Місто
    4. Країна
    -------------
    0. Повернутись до головного меню
    '''
    while True:
        selected_field = input(CHOICE_FIELD_TEXT)
        choice_field_dict = {
            '1': ("Ім'я", "first name"),
            '2': ("Прізвище", "last name"),
            '3': ("Місто", "city"),
            '4': ("Країна", "state")
        }
        if int(selected_field) in range(1, 5):
            current_number_data[choice_field_dict[selected_field][1]] = field_validator(choice_field_dict[selected_field][0])
            phonebook_container[phone_number] = current_number_data
            another_change = input('Бажаєте внести зміни в інше поле?(y/n): ')
            if another_change == 'y':
                continue
            elif another_change == 'n':
                break
        elif selected_field == '0':
            return
        else:
            print('Невірно вибране поле.')

    with open('phonebook.json', 'w') as phonebook_file:
        json.dump(phonebook_container, phonebook_file)

    print("Дані оновлено успішно!")


def delete_number():
    phone_number = number_entry()
    with open('phonebook.json', 'r') as phonebook_file:
        phonebook_container = json.load(phonebook_file)

    if not is_number_in_phonebook(phonebook_container, phone_number):
        print('Такого номеру немає у базі')
        return
    else:
        phonebook_container.pop(phone_number)

    with open('phonebook.json', 'w') as phonebook_file:
        json.dump(phonebook_container, phonebook_file)

    print("Номер видалено успішно!")


def is_number_in_phonebook(phone_number_dict, phone_number):
    number_list = [number for number in phone_number_dict]
    if phone_number in number_list:
        return True
    else:
        return False


def add_number_data():
    data_name_list = [("Ім'я", "first name"), ("Прізвище", "last name"), ("Місто", "city"), ("Країна", "state")]
    data_final_dict = dict()
    for field in data_name_list:
        field_value = field_validator(field[0])
        data_final_dict[field[1]] = field_value
    return data_final_dict


def number_entry():
    is_number_valid = False
    while not is_number_valid:
        phone_number = input(f"Введіть номер телефону: ")
        is_number_valid = (phone_number.isnumeric() or (phone_number[0] == '+' and phone_number[1:].isnumeric())) \
                          and len(phone_number) <= 15
        if not is_number_valid:
            print("Номер не є валідним!")
    return phone_number


def field_validator(field):
    is_field_valid = False
    while not is_field_valid:
        field_value = input(f"Введіть значення для поля {field}: ")
        is_field_valid = field_value.replace(" ", "").replace("-", "").replace(".", "").isalpha()
        if not is_field_valid:
            print("Це значення не є валідним!")
    return field_value


def find_by_number(container):
    phone_number = number_entry()
    for key, value in container.items():
        if key == phone_number:
            phone_number_string = f'За номером телефону {key} знайдено наступний запис\n {value}'
            print(phone_number_string)
            return
    else:
        print('Такого номеру немає у базі')


def find_by_name(container):
    name = field_validator("Ім'я")
    result_dict = dict()
    for key, value in container.items():
        if value['first name'] == name:
            result_dict[key] = value
    if not result_dict:
        print("Записів з таким ім'ям немає у базі")
    else:
        print(f"За ім'ям {name} знайдено наступні записи:\n{result_dict}")


def find_by_surname(container):
    surname = field_validator('Прізвище')
    result_dict = dict()
    for key, value in container.items():
        if value['last name'] == surname:
            result_dict[key] = value
    if not result_dict:
        print("Записів з таким ім'ям немає у базі")
    else:
        print(f"За прізвищем {surname} знайдено наступні записи:\n{result_dict}")


def find_by_fullname(container):
    name = field_validator("Ім'я")
    surname = field_validator('Прізвище')
    fullname = name + ' ' + surname
    result_dict = dict()
    for key, value in container.items():
        if (value['first name'] == name and value['last name'] == surname):
            result_dict[key] = value
    if not result_dict:
        print("Записів з таким ім'ям немає у базі")
    else:
        print(f"За ім'ям {fullname} знайдено наступні записи: \n{result_dict}")


def find_by_city_state(container):
    city_state = field_validator('Місто або Країна')
    result_dict = dict()
    for key, value in container.items():
        if (value['city'] == city_state or value['state'] == city_state):
            result_dict[key] = value
    else:
        print("Записів з таким ім'ям немає у базі")
    print(f"У результаті пошуку за значенням {city_state} знайдено наступні записи: \n{result_dict}")