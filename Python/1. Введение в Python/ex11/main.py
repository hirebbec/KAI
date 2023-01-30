from random import random, randint

num = randint(1, 10)
ans = int(input("Введите число: "))
count = 1;
while ans != num:
    if ans < num:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif ans > num:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    ans = int(input("Введите число: "))
    count += 1
print("Вы угадали! Число попыток: ", count)