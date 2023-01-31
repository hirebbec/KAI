#Определяем функцию
def func(_list):
    return [num if num >= 0 else 0 for num in _list]
#Проверка
_list =  [1.1, -0.12, 3.12, -0.99, -2,22, 2.88, -2.92, 1.16, 4.2]
print(func(_list))