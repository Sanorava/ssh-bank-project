account_card = input()


def mask_account_card(account_card: str) -> str:
    """
    функция, которая принимает название и номер счета и возвращает скрытый номер
    """

    splited_str = account_card.split()

    mask_need_string = splited_str[-1]

    masked_number = mask_need_string.replace(mask_need_string[6:11], "******")

    del splited_str[-1]

    print(" ".join(splited_str), masked_number)


mask_account_card(account_card)
