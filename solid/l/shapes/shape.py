class Shape:
    def get_area(self):
        print("SHAPE")


class Sides:
    def set_h(self, height: float):
        pass

    def set_w(self, width: float):
        pass


class Equilateral:
    def set_side(self, side: float):
        pass


class Rectangle(Shape, Sides):
    def __init__(self):
        self.height = 0
        self.width = 0

    def set_h(self, height: float):
        self.height = height

    def set_w(self, width: float):
        self.width = width

    def get_area(self):
        print("RECT")
        return self.width * self.height


class Square(Shape, Equilateral):
    def __init__(self):
        self.side = 0

    def set_side(self, side: float):
        self.side = side

    def get_area(self):
        return self.side * self.side


class User:
    @staticmethod
    def find_area(shape: Shape):
        return shape.get_area()


rec = Rectangle()
rec.set_w(100)
rec.set_h(10)
print(User.find_area(rec))






