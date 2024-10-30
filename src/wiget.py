from datetime import datetime

account_card = input()


def mask_account_card(account_card: str) -> str:
    """
    функция, которая принимает название и номер счета и возвращает скрытый номер
    """

    splited_str = account_card.split()

    mask_need_string = splited_str[-1]

    if splited_str[0] == "Счет" or splited_str[0] == "Счёт":

        masked_number = mask_need_string.replace(mask_need_string[:-4], "**")

        del splited_str[-1]

        return " ".join(splited_str) + " " + masked_number

    else:

        masked_number = mask_need_string.replace(mask_need_string[6:11], "******")

        parts = [masked_number[i:i + 4] for i in range(0, 16, 4)]

        final_number = ' '.join(parts)

        del splited_str[-1]

        return " ".join(splited_str) + " " + final_number


print(mask_account_card(account_card))


def get_date(date_string: str) -> str:
    """
    Функция форматирующая дату
    """

    date_obj = datetime.fromisoformat(date_string)

    # Форматируем объект datetime в нужный формат
    formatted_date = date_obj.strftime("%d.%m.%Y")

    return formatted_date
