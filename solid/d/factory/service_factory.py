from service import Service, ServiceConcreteImpl

class ServiceFactory:
    def create_service(self, service: str):
        pass


class ServiceFactoryImpl(ServiceFactory):
    def create_service(self, service: str) -> Service:
        if service == "ServiceA":
            # 建立 ServiceA
            return ServiceConcreteImpl()
        elif service == "ServiceB":
            # 建立 ServiceB
            pass
        else:
            # 建立 ServiceC
            pass











