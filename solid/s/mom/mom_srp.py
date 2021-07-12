from enum import Enum, auto


class Service:
    pass


class CookService(Service):
    def cook(self):
        print("Cooking")


class FeedingTarget(Enum):
    baby = auto()
    cat = auto()


class FeedService(Service):
    def feed_baby(self):
        print("Feeding Baby")

    def feed_cat(self):
        print("Feeding Cat")


class WorkService(Service):
    def work(self):
        print("Working")


class Mom:
    def __init__(self, name: str = "Mom"):
        self.name = name

    def do_chores(self, service: Service, target: FeedingTarget = None):
        print(f"{self.name} is currently")
        if isinstance(service, CookService):
            service.cook()
        elif isinstance(service, FeedService):
            if target is FeedingTarget.baby:
                service.feed_baby()
            elif target is FeedingTarget.cat:
                service.feed_cat()
        elif isinstance(service, WorkService):
            service.work()

    # ... more activities


mom = Mom()
mom.do_chores(WorkService())










