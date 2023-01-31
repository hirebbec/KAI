#Создаем анонимную функцию и вызываем ее в мапе
list = list(map(lambda num: num ** 2, range(0, 11)))
#Проверка
print(list)