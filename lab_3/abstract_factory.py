from abc import ABC, abstractmethod


class Window(ABC):
    @abstractmethod
    def draw(self):
        pass


class ScrollBar(ABC):
    @abstractmethod
    def draw(self):
        pass


class LightWindow(Window):
    def draw(self):
        print("Light window: белый фон, тёмные границы")


class LightScrollBar(ScrollBar):
    def draw(self):
        print("Light scrollbar: тонкий, светлый")


class DarkWindow(Window):
    def draw(self):
        print("Dark window: тёмный фон, светлые элементы")


class DarkScrollBar(ScrollBar):
    def draw(self):
        print("Dark scrollbar: толстый, тёмный")


class ThemeFactory(ABC):
    @abstractmethod
    def create_window(self) -> Window:
        pass

    @abstractmethod
    def create_scrollbar(self) -> ScrollBar:
        pass


class LightThemeFactory(ThemeFactory):
    def create_window(self) -> Window:
        return LightWindow()

    def create_scrollbar(self) -> ScrollBar:
        return LightScrollBar()


class DarkThemeFactory(ThemeFactory):
    def create_window(self) -> Window:
        return DarkWindow()

    def create_scrollbar(self) -> ScrollBar:
        return DarkScrollBar()


class Application:
    def __init__(self, factory: ThemeFactory):
        self.window = factory.create_window()
        self.scrollbar = factory.create_scrollbar()

    def render(self):
        self.window.draw()
        self.scrollbar.draw()


if __name__ == "__main__":
    print("* Light Theme *")
    app_light = Application(LightThemeFactory())
    app_light.render()

    print("* Dark Theme *")
    app_dark = Application(DarkThemeFactory())
    app_dark.render()
