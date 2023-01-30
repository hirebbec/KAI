alphabet = 'абвгдеёжзи'
#Копия
print(alphabet)
#Реверснутая копия
print(alphabet[::-1]);
#Каждый второй символ
for i in range(0, len(alphabet), 2):
    print(alphabet[i], end='')
print()
#Каждый второй символ после 1
for i in range(1, len(alphabet), 2):
    print(alphabet[i], end='')
print()
#Все элементы до 5
for i in range(0, 4, 1):
    print(alphabet[i], end='')
print()
#Все элементы в диапазоне от 2 до 6
for i in range(2, 6, 1):
    print(alphabet[i], end='')
print()
#Последние 3 элемента
for i in range(len(alphabet) - 3, len(alphabet), 1):
    print(alphabet[i], end='')
print()
#Эленменты от 3 до 4 в обратном порядке
for i in range(4, 1, -1):
    print(alphabet[i], end='')
print()