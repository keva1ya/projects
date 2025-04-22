class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)
x1 = int(input("x1->"))
y1 = int(input("y1->"))
x2 = int(input("x2->"))
y2 = int(input("y2->"))
p1 = Point(x1, y1)
p2 = Point(x2, y2)
p3 = p1.add(p2)
print(f"P3: ({p3.x}, {p3.y})")
