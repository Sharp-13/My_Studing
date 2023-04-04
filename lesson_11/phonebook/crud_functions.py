import json

def create_number():

    phone_number = number_entry()

    with open('phonebook.json', 'r') as phonebook_file:
        phonebook_container = json.load(phonebook_file)

    if find_by_number(phonebook_container, phone_number):
        print('Такий номер вже є у базі')
        return
    else:
        phonebook_container[phone_number] = add_number_data()

    with open('phonebook.json', 'w') as phonebook_file:
        json.dump(phonebook_container, phonebook_file)
    print('Запис додано успішно!')


def find_number():
    phone_number = number_entry()
    with open('phonebook.json', 'r') as phonebook_file:
        phonebook_container = json.load(phonebook_file)



def update_number():
    phone_number = number_entry()
    with open('phonebook.json', 'r') as phonebook_file:
        phonebook_container = json.load(phonebook_file)

    if not find_by_number(phonebook_container, phone_number):
        print('Такого номеру немає у базі')
        return
    else:
        current_number_data = phonebook_container.pop(phone_number)
    CHOICE_FIELD_TEXT = '''Будь ласка, вкажіть поле, в яке Ви хотіли б внести зміни:
    1. First name
    2. Last name
    3. City
    4. State
    '''
    selected_field = input(CHOICE_FIELD_TEXT)
    choice_field_dict = {
        '1': 'First name',
        '2': 'Last name',
        '3': 'City',
        '4': 'State'
    }
    current_number_data[choice_field_dict[selected_field]] = field_validator(choice_field_dict[selected_field])
    phonebook_container[phone_number] = current_number_data

    with open('phonebook.json', 'w') as phonebook_file:
        json.dump(phonebook_container, phonebook_file)

    print("Дані оновлено успішно!")


def delete_number():
    phone_number = number_entry()
    with open('phonebook.json', 'r') as phonebook_file:
        phonebook_container = json.load(phonebook_file)

    if not find_by_number(phonebook_container, phone_number):
        print('Такого номеру немає у базі')
        return
    else:
        current_number_data = phonebook_container.pop(phone_number)

    with open('phonebook.json', 'w') as phonebook_file:
        json.dump(phonebook_container, phonebook_file)

    print("Номер видалено успішно!")


def find_by_number(phone_number_dict, phone_number):
    number_list = [number for number in phone_number_dict]
    if phone_number in number_list:
        return True
    else:
        return False


def add_number_data():
    data_name_list = ["First name", "Last name", "City", "State"]
    data_final_dict = dict()
    for field in data_name_list:
        field_value = field_validator(field)
        data_final_dict[field] = field_value
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
            print("Це поле не є валідним!")
    return field_value