from rectangle import Rectangle, Square


class User:

    @staticmethod
    def find_area_of_rect(rect: Rectangle):
        rect.set_h(100)
        rect.set_w(50)
        assert (rect.get_area()) == 5000

    @staticmethod
    def fixed_find_area_of_rect(rect: Rectangle):
        rect.set_h(100)
        rect.set_w(50)

        if isinstance(rect, Rectangle):
            assert (rect.get_area()) == 5000
        elif isinstance(rect, Square):
            assert (rect.get_area()) == 2500

        if isinstance(rect, Square):
            assert (rect.get_area()) == 2500
        elif isinstance(rect, Rectangle):
            assert (rect.get_area()) == 5000


User.find_area_of_rect(Rectangle())

User.find_area_of_rect(Square())

