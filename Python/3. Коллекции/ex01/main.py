#Импорты
import random as rnd
#Создание списка
list = []
for _ in range(10):
    list.append(rnd.randint(0, 20))
#Сортировка при помощи встроенных функций
sorted_list = sorted(list)
#Сортировка пузырьковым методом
my_list = list.copy()
flag = True
while flag == True:
    flag = False
    for i in range(len(my_list) - 1):
        if (my_list[i] > my_list[i + 1]):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] #SWAP
            flag = True
#Проверка
print('Начальный список: ', list)
print('Список отсортированный встроенной функцией: ', sorted_list)
print('Список отсортированный вручную: ', my_list)