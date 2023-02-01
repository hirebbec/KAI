from Circle import Circle
#Test
circle1 = Circle(0, 0, 3)
circle2 = Circle(1, 1, 1)
circle3 = Circle(1, 1, 3)
circle4 = Circle(10, 10, 3)
circle5 = Circle(0, 4, 2)
circle6 = Circle(0, 4, 1)
circle7 = Circle(1, 1, 2)
circle8 = Circle(0, 0, 3)
circle9 = Circle(0, 3, 1)
circle10 = Circle(0, 3, 10)
print(circle1.checkCroosing(circle2))  # One circle is inside the other and does not intersect
print(circle1.checkCroosing(circle3))  # One circle is inside another and intersects
print(circle1.checkCroosing(circle4))  # Circles are not nested and do not intersect
print(circle1.checkCroosing(circle5))  # Circles are not nested and intersect
print(circle1.checkCroosing(circle6))  # The circles are not nested and touch each other (count as an intersection)
print(circle1.checkCroosing(circle7))  # One circle is inside another and they touch each other (count as an intersection)
print(circle1.checkCroosing(circle8))  # Two identical circles
print(circle1.checkCroosing(circle9))  # The circle lies on the border of another, its radius is less than the main one.
print(circle1.checkCroosing(circle10))  # The circle lies on the border of another, its radius is greater than the main one.