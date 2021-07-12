class Pizza:
    def __init__(self):
        self.is_baked = False
        self.is_prepared = False
        self.ingredients = ["cheese", "sausage", "olive", "flower"]
        self.name = "Pizza"


class PizzaMakingService:
    def make_pizza(self, pizza, callback):
        raise NotImplemented("make_pizza should be implemented")


class PizzaMaker(PizzaMakingService):
    def make_pizza(self, pizza, callback):
        pizza = self._prepare_pizza(pizza)
        pizza = self._bake_pizza(pizza)
        callback(self._box_pizza(pizza))

    def _prepare_pizza(self, pizza: str) -> Pizza:
        return Pizza()

    def _bake_pizza(self, pizza) -> Pizza:
        pizza.is_baked = True
        return pizza

    def _box_pizza(self, pizza) -> Pizza:
        pizza.is_prepared = True
        return pizza


class PizzaCompany:
    def order_pizza(self, pizza, pizza_maker: PizzaMaker):
        pizza_maker.make_pizza(pizza, self.deliver_pizza)

    def deliver_pizza(self, pizza):
        pass





