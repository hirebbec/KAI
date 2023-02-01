class House:
    
    __doc__ = f"Documentation: something.."
    
    def __init__(self, count, color, balkony):
        self._count = count
        self._color = color
        self._balkony = balkony

    def __str__(self):
        return f"Floor count: {self._count}\nColor: {self._color}\nBalcony: {self._balkony}"

    def setCount(self, count):
        self._count = count

#Main
house = House(5, 'red', False)
print(house)
print(house.__doc__)
print('------------------')
house.setCount(10)
print(house)