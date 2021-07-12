from service import Service
from service_factory import ServiceFactory


class Application:
    def __init__(self, service_factory: ServiceFactory):
        self.service_factory = service_factory
        self.service: Service = None
        self.prepare_service()

    def prepare_service(self):
        self.service = self.service_factory.create_service("ServiceA")

    def perform_service_task(self):
        self.service.do_something()









