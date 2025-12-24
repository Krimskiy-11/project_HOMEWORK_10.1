def filter_by_state(my_lists: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий словари,
    у которых state соответствует указанному значению"""

    result_list = list()

    for i in my_lists:
        if i["state"] == state:
            result_list.append(i)

    return result_list


def sort_by_date(my_lists: list[dict], reverse: bool = True) -> list[dict]:
    """Функция возвращает новый список словарей, отсортированный по дате"""

    sorted_dict = sorted(my_lists, key=lambda i: i["date"], reverse=reverse)
    return sorted_dict
