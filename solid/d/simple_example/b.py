import time


class BService:
    def perform_a_task(self):
        pass


class B:
    def __init__(self, name):
        self.name = name

    def perform_a_task(self):
        print("Performing a task")


class B1(BService):
    def __init__(self, name):
        self.name = name

    def perform_a_task(self):
        time.sleep(1)
        print("Perform a task after a second")


class B2(BService):
    def __init__(self, name):
        self.name = name

    def perform_a_task(self):
        time.sleep(2)
        print("Perform a task after a second")


class B3:
    def __init__(self, name):
        self.name = name

    def perform_a_task(self):
        time.sleep(3)
        print("Perform a task after a second")





