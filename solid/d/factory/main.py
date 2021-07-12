from service_factory import ServiceFactoryImpl
from application import Application

app = Application(ServiceFactoryImpl())

app.perform_service_task()
