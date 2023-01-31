#Импорты
from functools import wraps
#Определяем декаратор для запсии в файл 'log.txt'
def decorator_1(func):
    wraps(func)
    def wrapper(_list):
        result = func(_list)
        with open('log.txt', 'w') as file:
            file.write(str(result))
        return result
    return wrapper

#Определяем декаратор для запсии в указанный файл
def decorator_2(filename):
    def decorator(func):
        wraps(func)
        def wrapper(_list):
            result = func(_list)
            with open(filename, 'w') as file:
                file.write(str(result))
            return result
        return wrapper
    return decorator


#Применяем первый декоратор
@decorator_1
@decorator_2('lol.txt')
def summator(nums_list):
    return sum(nums_list)

#Проверка
print(summator(range(10)))