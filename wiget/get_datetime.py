from datetime import datetime


def get_date(date_string: str) -> str:
    """
    Функция форматирующая дату
    """

    date_obj = datetime.fromisoformat(date_string)

    # Форматируем объект datetime в нужный формат
    formatted_date = date_obj.strftime("%d.%m.%Y")

    return formatted_date
