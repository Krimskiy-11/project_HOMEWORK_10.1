from masks import get_mask_card_number, get_mask_account
from typing import Union


def mask_account_card(card_or_account: str) -> Union[str|None]:
    list_card_or_account = card_or_account.split()
    for i in list_card_or_account:
        if i.isdigit():
            len_num = len(i)
            if len_num == 20:
                return get_mask_account(i)
            elif len_num == 16:
                return get_mask_card_number(i)


def get_date(date: str) -> str:
    normal_date = date[:10]
    list_normal_date = normal_date.split("-")
    return f"{list_normal_date[2]}.{list_normal_date[1]}.{list_normal_date[0]}"
