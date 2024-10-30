from datetime import datetime


def filter_by_state(data: dict, state='EXECUTED') -> dict:
    """
    Функция фильтрует список словарей по ключу 'state'.

    data: Список словарей для фильтрации.
    state: Значение для ключа state, по которому будет производиться фильтрация.
    return Новый список словарей, соответствующих заданному значению для ключа state.
    """
    filtered_data = [item for item in data if item.get('state') == state]
    return filtered_data


def sort_by_date(data, ascending=False):
    """
    Функция сортирует список словарей по ключу date.

    data: Список словарей, содержащих дату в формате 'YYYY-MM-DD'.
    ascending: Порядок сортировки; если True, сортировка по возрастанию, если False - по убыванию (по умолчанию).
    return Новый отсортированный список словарей.
    """
    # Делаем сортировку на основе ключа 'date'
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=not ascending)
    return sorted_data