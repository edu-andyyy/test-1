from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class TenPercentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.9


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply(self, total: float) -> float:
        return max(0.0, total - self.amount)


class ShoppingCart:
    def __init__(self, items: list[float]):
        self.items = items
        self.strategy: DiscountStrategy = NoDiscount()

    def set_strategy(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def total(self) -> float:
        raw = sum(self.items)
        return self.strategy.apply(raw)


if __name__ == "__main__":
    cart = ShoppingCart([10.0, 20.0, 30.0])  # 60.0

    cart.set_strategy(NoDiscount())
    print(cart.total())  # 60.0

    cart.set_strategy(TenPercentDiscount())
    print(cart.total())  # 54.0

    cart.set_strategy(FixedAmountDiscount(15.0))
    print(cart.total())  # 45.0
