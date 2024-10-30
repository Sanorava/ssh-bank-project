def filter_by_state(data: dict, state='EXECUTED') -> dict:
    """
    Функция фильтрует список словарей по ключу 'state'.

    data: Список словарей для фильтрации.
    state: Значение для ключа state, по которому будет производиться фильтрация.
    return Новый список словарей, соответствующих заданному значению для ключа state.
    """
    filtered_data = [item for item in data if item.get('state') == state]
    return filtered_data