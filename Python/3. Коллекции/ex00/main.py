#Считывание числа с консоли
num = int(input("Ведите число: "))
#Формирование списка
list = []
i = 1
while (i <= num):
    list.append(i)
    i += 2
#Проверка
print(list)
