class Service:
    def do_something(self):
        print("Default Do Something")


class Application:
    def perform_service_task(self, service: Service):
        service.do_something()


class OwnApplication:
    def __init__(self, service: Service):
        self.service = service

    def perform_service_task(self):
        self.service.do_something()