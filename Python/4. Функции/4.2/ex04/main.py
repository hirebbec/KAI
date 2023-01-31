#Генератор для получения числа из файла
def next_num(filename):
    with open(filename, 'r') as file:
        letter = file.read(1)
        while letter:
            num = letter
            letter = file.read(1)
            while letter != ' ' and letter:
                num += letter
                letter = file.read(1)
            yield num
            letter = file.read(1)

#генератор для складывания чисел
def summator():
    sum = 0
    while  True:
        num = yield sum
        if not num: break
        sum += int(num) 

#Определяем генераторы
sum_generator = summator()
num_generator = next_num('numbers.txt')
#"Запускаем" Генератор? Хз как это еще назвать
next(sum_generator)

#Читаем числа пока не закончаться и выброситься исключение
while True:
    print(sum_generator.send(next(num_generator)))


