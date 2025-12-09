def get_mask_card_number(card_num: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""

    mask = card_num.replace(card_num[6:12], "******")

    space_card_num = ""
    for i in mask:
        space_card_num += i
        if len(space_card_num) == 4 or len(space_card_num) == 9 or len(space_card_num) == 14:
            space_card_num += " "

    return space_card_num


def get_mask_account(total_num: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""

    return total_num.replace(total_num[:-4], "**")
