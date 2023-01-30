#Определим функицю
def gretting(name, age = None, gretting = "Добро пожаловать"):
    if (name.isalpha() == True):
        print(name, age, gretting)

#Тесты
gretting("Ильдар")
gretting("Ильдар", 14)
gretting("Ильдар", 14, "Салам алейкум")

