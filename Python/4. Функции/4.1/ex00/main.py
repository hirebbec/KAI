#Определим функцию
def  my_split(_str):
    return _str.split()

#Принимаем начальную строку
text = input("Введите текск: ")
#Вызываем нашу функцию
list = my_split(text)
#Проверка
print(list)