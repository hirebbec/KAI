import math

class Circle:
    def __init__(self, x = 0, y = 0, r = 1):
        self._x = x
        self._y = y
        self._r = r
    
    def __str__(self) -> str:
        return f"Center x: {self._x}\nCenter y: {self._y}\nRadius: {self._r}\n"

    def getArea(self):
        return math.pi * (self._r ** 2)

    def getPerimeter(self):
        return 2 * math.pi * self._r

    def checkCroosing(self, other):
        distance_between_centers = math.sqrt(abs(self._x ** 2 - other._x** 2) + abs(self._y ** 2 - other._y** 2))
        if (distance_between_centers < max(self._r, other._r)): # When one circle is inside another
            return self._inside(other, self) if (self._r >= other._r) else self._inside(self, other)
        elif (distance_between_centers == max(self._r, other._r)):  # The case when the center of one circle is on the boundary of the second
            return True
        else:  # The case when the circles are not nested one into the other
            return (self._r + other._r) >= distance_between_centers if True else False  # The case when the circles are not nested in each other

    def _inside(self, in_, out_):
        distance_between_centers = math.sqrt(abs(out_._x ** 2 - in_._x** 2) + abs(out_._y ** 2 - in_._y** 2))
        return True if (distance_between_centers + in_._r) >= out_._r else False