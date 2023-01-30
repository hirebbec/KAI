#Данные
ids = {
    't-shirt': '10',
    'sneakers': '20',
    'trousers': '30',
    'cap': '40',
    'jacket': '50'
}
store = {
    '10': [
        {'quantity': 50, 'price': 800},
        {'quantity': 70, 'price': 950},
    ],
    '20': [
        {'quantity': 6, 'price': 5000},
        {'quantity': 12, 'price': 6000},
        {'quantity': 18, 'price': 4500},
    ],
    '30': [
        {'quantity': 22, 'price': 1200},
        {'quantity': 50, 'price': 1150},
    ],
    '40': [
        {'quantity': 5, 'price': 600},
    ],
    '50': [
        {'quantity': 11, 'price': 15000},
    ]
}
#Внешний цикл для итерирования в первом словаре
for product in ids:
    #Переменные для счета
    count = 0
    price = 0
    #id товара
    product_id = ids[product]
    if product_id in store:#проверка на наличие товара в магазине
        for data in store[product_id]:# внутренний цикл по продуктам с нужныйм id
            count += data['quantity']
            price += data['price'] * data['quantity']
        print(product, '-', count, 'pieces, worth', price, 'rub')