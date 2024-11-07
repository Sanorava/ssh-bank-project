from functools import wraps


def log(filename = None):
    def my_decorator(func):
        print('DEBUG_1', 'я вызываюсь перед шагом, который вызывает мою функцию для логирования')
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


@log('..\log\logs.txt')
def my_function(x, y):
    return x + y
print(my_function(1, '2'))