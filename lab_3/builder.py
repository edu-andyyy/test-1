from abc import ABC, abstractmethod


class Sandwich:
    def __init__(self):
        self.bread = None
        self.filling = None
        self.sauce = None

    def __str__(self):
        return f"Sandwich(bread={self.bread}, filling={self.filling}, sauce={self.sauce})"


class SandwichBuilder(ABC):
    @abstractmethod
    def set_bread(self):
        pass

    @abstractmethod
    def set_filling(self):
        pass

    @abstractmethod
    def set_sauce(self):
        pass

    @abstractmethod
    def get_result(self) -> Sandwich:
        pass


class BLTBuilder(SandwichBuilder):
    def __init__(self):
        self.sandwich = Sandwich()

    def set_bread(self):
        self.sandwich.bread = "тостовый хлеб"

    def set_filling(self):
        self.sandwich.filling = "бекон, салат, помидор"

    def set_sauce(self):
        self.sandwich.sauce = "майонез"

    def get_result(self) -> Sandwich:
        return self.sandwich


class VeggieBuilder(SandwichBuilder):
    def __init__(self):
        self.sandwich = Sandwich()

    def set_bread(self):
        self.sandwich.bread = "цельнозерновой"

    def set_filling(self):
        self.sandwich.filling = "авокадо, огурец, шпинат"

    def set_sauce(self):
        self.sandwich.sauce = "хумус"

    def get_result(self) -> Sandwich:
        return self.sandwich


class SandwichDirector:
    def __init__(self, builder: SandwichBuilder):
        self.builder = builder

    def build(self) -> Sandwich:
        self.builder.set_bread()
        self.builder.set_filling()
        self.builder.set_sauce()
        return self.builder.get_result()


if __name__ == "__main__":
    blt = SandwichDirector(BLTBuilder()).build()
    print(blt)

    veggie = SandwichDirector(VeggieBuilder()).build()
    print(veggie)
