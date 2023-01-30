from random import random, randint

num = int(input("Загадайте число: "))
ans = randint(1, 10)
msg = ""
while (msg.lower() != "равно"):
    print("Твое число больше, равно или меньше, чем число ", ans)
    msg = str(input())
    if msg.lower() == "больше":
        ans += randint(1, 10)
    elif msg.lower() == "меньше":
        ans -= randint(1, 10)