class Vector:
    __slots__ = ('vx', 'vy')

    def __init__(self, init_vx=0, init_vy=0):
        self.vx = init_vx
        self.vy = init_vy

    def add_vector(self, vector):
        self.vx += vector.vx
        self.vy += vector.vy
