num = int(input("Введите год:"))
if (num % 400 == 0 or (num % 4 == 0 and num % 100 != 0)):
    print("Год високосный")
else:
    print("Год не високосный")