#Объявление и нициализация словаря
beatles_map = {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}
#Добавляем в словарь музыканта
beatles_map['Ringo'] = "Drums"
#Запоминаем инструмент
instrument = beatles_map['John']
#Удаляем музыканта
beatles_map.pop('John')
#Проверка
print(beatles_map)
print(instrument)
