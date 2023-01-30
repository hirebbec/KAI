#Открываем файл
file = open('numbers.txt', 'r')
#Считываем числа
numbers = file.readlines()
#Считаем сумму
sum = 0
for num in numbers:
    sum += int(num)
#Записывем ответ
out = open('answer.txt', 'w')
out.write(str(sum))
file.close()
out.close()