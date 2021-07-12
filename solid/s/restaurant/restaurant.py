class Restaurant:
    def write_order(self):
        print("Writing Order")

    def prepare_food(self, food):
        print(f"Preparing {food}")

    def deliver_food(self, food):
        print(f"Delivering {food}")

    # more actions ...


class RestaurantFacade:

    def __init__(self):
        self.cook = Cook()
        self.waiter = Waiter()

    def order_food(self, order: list):
        foods = self.waiter.write_order(order)
        self.cook.prepare_food(foods,
                               self.waiter.deliver_food)

    # more actions ...


class Cook:
    def prepare_food(self, foods: list,
                     food_callback):
        for food in foods:
            print(f"Preparing {food}")
            import time
            time.sleep(1)
            print(f"Done Preparing {food}")
            food_callback(food)


class Waiter:
    def write_order(self, orders) -> [str]:
        print("Writing Orders")
        # return Foods
        return orders

    def deliver_food(self, food):
        print(f"Delivering {food}")
        print("============================")


res = RestaurantFacade()
res.order_food(["fish", "chicken"])
