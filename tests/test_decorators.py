from calendar import error
from functools import wraps
from re import match

import pytest


def log(filename = None):
    """
    Создал декоратор, который вызывает функцию для декорации и записывает результат в файл,
    если тот передан в аргумент декоратора, иначе же- выводит сообщение в консоль.

    Если функция отработала корректно- выведет\запишет сообщение ' имя функции ок'
    иначе выведет\запишет тип ошибки.

    """
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} ok\n')
                else:
                    print(f'{func.__name__} ok\n')
            except Exception as e:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} ERROR : {e.__class__.__name__}. Inputs: {args}, {kwargs}\n')
                else:
                    print(f'{func.__name__} ERROR : {e.__class__.__name__}. Inputs: {args}, {kwargs}\n')
        return wrapper
    return my_decorator


@log()
def example_func():
    raise ValueError


def test_log():
    with pytest.raises(Exception, match = f'{example_func.__name__} ERROR : {e.__class__.__name__}. Inputs: \n'):
        example_func()