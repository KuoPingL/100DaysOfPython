class Rectangle:
    def __init__(self):
        self.height = 0
        self.width = 0

    def set_h(self, height: float):
        self.height = height

    def set_w(self, width: float):
        self.width = width

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_h(self, height: float):
        self.height = height
        self.width = height

    def set_w(self, width: float):
        self.width = width
        self.height = width

