class A:
    def a_do_something(self):
        pass


class B:
    def __init__(self):
        self.a = A()

    def b_do_something(self):
        pass


def take_in_c(b: B):
    take_in_a(b.a)


def take_in_a(a: A):
    a.a_do_something()



