url = str(input("url:"))
if (url.startswith("https") == False):
    print("Ошибка: адрес не начинается с https.")
elif (url.find("documentlibrary") == -1):
    print("Ошибка: подстрока documentlibrary не обнаружена.")
else:
    print("Адрес указан верно.")