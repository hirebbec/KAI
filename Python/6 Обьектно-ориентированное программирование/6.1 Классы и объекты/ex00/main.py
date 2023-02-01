class House:
    
    __doc__ = 'Something...'
    
    def __init__(self, count, color, balkony):
        self.count = count
        self.color = color
        self.balkony = balkony

    def __str__(self):
        return 'Color = {}\nCount = {}\nBalkony = {}'.format(self.color, self.count, self.balkony)

#Main
house = House(5, 'red', False)
print(house)
print(house.__doc__)