import math

N = int(input("Введите число:"))
for i in range(1, N + 1, 2):
    print(int(math.pow(i, 5)))