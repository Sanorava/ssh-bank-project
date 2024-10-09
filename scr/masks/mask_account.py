account_number = input()


def get_mask_account(account_number: str) -> str:
    """
    Функция, которая маскирует номер лицевого счета
    """

    masked_account_number = account_number.replace(account_number[0:16], "**")

    return masked_account_number


get_mask_account(account_number)
