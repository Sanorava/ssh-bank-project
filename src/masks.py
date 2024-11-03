def get_mask_card_number(card_number: str) -> str:
    """
    Функция, которая делит строку на 4 части и маскирует блок цифр
    """

    new_card_number = card_number.replace(card_number[6:12], "******")

    parts = [new_card_number[i : i + 4] for i in range(0, 16, 4)]

    splited_number = " ".join(parts)

    return splited_number


get_mask_card_number


def get_mask_account(account_number: str) -> str:
    """
    Функция, которая маскирует номер лицевого счета
    """

    masked_account_number = account_number.replace(account_number[0:16], "**")

    return masked_account_number


get_mask_account
