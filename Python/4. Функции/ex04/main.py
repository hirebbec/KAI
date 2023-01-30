#Импорты
import os.path
abs_path = os.path.abspath('numbres.txt')
local_path = os.path.join('./', 'numbers.txt')
print("Абсолютный путь: ", abs_path) 
print("Относительный путь: ", local_path)