#Создаем функцию
def to_str(_list):
    return list(map(str, _list))
#Проверка
print(to_str(range(10)))