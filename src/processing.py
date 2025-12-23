def filter_by_state(my_lists: list[dict], state='EXECUTED') -> list[dict]:
    """ Функция возвращает новый список словарей, содержащий словари,
    у которых state соответствует указанному значению"""

    result_list = list()

    for dicts in my_lists:
        if dicts['state'] == state:
            result_list.append(dicts)

    return result_list

