#Импорты
import random as rnd
import string
#Создаем случайные списки
list1 = []
list2 = []
#Заполняем списки случайными буквами
first_list_len = rnd.randint(10, 15)
second_list_len = rnd.randint(10, 15)
for i in range(first_list_len):
    list1.append(rnd.choice(string.ascii_lowercase))
for i in range(second_list_len):
    list2.append(rnd.choice(string.ascii_lowercase))
#Создаем словари
dict1 = {}
dict2 = {}
#Инициализируем словари
for i in range(first_list_len):
    dict1[i] = list1[i]
for i in range(second_list_len):
    dict2[i] = list2[i]
#Проверка
print("Первый список: ", list1)
print("Второй список: ", list2)
print("Первый словарь: ", dict1)
print("Второй словарь: ", dict2)