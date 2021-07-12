from b import B, B1, B2, BService


class A:
    def do_something_with_b(self, b: B):
        b.perform_a_task()

    def do_something_with_b_service(self, bs: BService):
        bs.perform_a_task()



