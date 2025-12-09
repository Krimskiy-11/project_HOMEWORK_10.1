from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_or_account: str) -> str:
    list_card_or_account = card_or_account.split()
    for i in list_card_or_account:
        if i.isdigit():
            lenght_num = len(i)
            if lenght_num == 20:
                mask = get_mask_account(i)
            elif lenght_num == 16:
                mask = get_mask_card_number(i)
    return mask




print(mask_account_card('Maestro 1596837868705199'))
print(mask_account_card('Счет 35383033474447895560'))
print(mask_account_card('MasterCard 7158300734726758'))