# Задача 1.1: конкатенація словників

# Напишіть програму, котра приймає на вхід два словника, заданих через змінні і повертає один словник, що є сумою перших двох

# Якщо в обох словниках повторюються ключі, але їхні величини відрізняються,
# то на місці значення треба створити список усіх значень з обох словників.

# Якщо в обох словниках повторюються ключі та їхні величини, треба залишати одну величину і не створювати список

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 2, "c": 4, "d": 5}

expected_dict = dict()

expected_dict_1 = {"a": 1, "b": 2, "c": [3, 4], "d": 5}

list_1 = [key_1 for key_1 in dict_1.keys()]
list_2 = [key_2 for key_2 in dict_2.keys()]

concat_set = set(list_1 + list_2)

for i in concat_set:
    if i in dict_1.keys() and i not in dict_2.keys():
        expected_dict[i] = dict_1[i]
    elif i in dict_2.keys() and i not in dict_1.keys():
        expected_dict[i] = dict_2[i]
    elif (i in dict_1.keys() and i in dict_2.keys()) and (dict_1[i] == dict_2[i]):
        expected_dict[i] = dict_1[i]
    else:
        expected_dict[i] = [dict_1[i], dict_2[i]]

assert expected_dict == expected_dict_1

# expected_dict_1 = {"a": 1, "b": 2, "c": [3, 4], "d": 5}

# Задача 1.1: конкатенація списку словників

# Напишіть програму, котра приймає на вхід список словників і зливає їх в один за правилами, зазначеними вище.

# dicts_list = [dict_1, dict_2, {"c": 5, "d": 5, "e": 5}]
#
# expected_dict_2 = {"a": 1, "b": 2, "c": [3, 4, 5], "d": 5, "e": 5}

dicts_list = [dict_1, dict_2, {"c": 5, "d": 5, "e": 5}]

expected_dict_2 = {"a": 1, "b": 2, "c": [3, 4, 5], "d": 5, "e": 5}

result_dict: dict = dict()

for dictionary in dicts_list:
    keys_list_dict = list(dictionary.keys())
    keys_list_result = list(result_dict.keys())

    keys_set = set(keys_list_dict + keys_list_result)

    for i in keys_set:
        if i in keys_list_dict and i not in keys_list_result:
            result_dict[i] = dictionary[i]
        elif i in keys_list_result and i not in keys_list_dict:
            result_dict[i] = result_dict[i]
        elif (i in keys_list_result and i in keys_list_dict) and (dictionary[i] == result_dict[i]):
            result_dict[i] = dictionary[i]
        elif isinstance(result_dict[i], list):
            result_dict[i] = result_dict[i] + [dictionary[i]]
        elif isinstance(dictionary[i], list):
            result_dict[i] = dictionary[i] + [result_dict[i]]
        else:
            result_dict[i] = [dictionary[i], result_dict[i]]

print(result_dict)