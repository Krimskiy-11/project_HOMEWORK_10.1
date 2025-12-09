def get_mask_card_number(card_num: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    str_card_num = str(card_num)

    mask = str_card_num.replace(str_card_num[6:12], "******")

    space_card_num = ""
    for i in mask:
        space_card_num += i
        if len(space_card_num) == 4 or len(space_card_num) == 9 or len(space_card_num) == 14:
            space_card_num += " "

    return space_card_num


def get_mask_account(total_num: int) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    str_total_num = str(total_num)

    mask = str_total_num.replace(str_total_num[:-4], "**")

    return mask
