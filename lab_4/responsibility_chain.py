class Handler:
    def __init__(self):
        self._next = None

    def set_next(self, handler: "Handler"):
        self._next = handler
        return handler

    def handle(self, value: int):
        handled = self._handle(value)
        if not handled and self._next:
            return self._next.handle(value)
        return handled

    def _handle(self, value: int) -> bool:
        raise NotImplementedError


class SmallHandler(Handler):
    def _handle(self, value: int) -> bool:
        if value < 10:
            print(f"SmallHandler {value}")
            return True
        return False


class MediumHandler(Handler):
    def _handle(self, value: int) -> bool:
        if 10 <= value < 100:
            print(f"MediumHandler {value}")
            return True
        return False


class LargeHandler(Handler):
    def _handle(self, value: int) -> bool:
        if value >= 100:
            print(f"LargeHandler {value}")
            return True
        return False


if __name__ == "__main__":
    h1 = SmallHandler()
    h2 = MediumHandler()
    h3 = LargeHandler()

    h1.set_next(h2).set_next(h3)

    for v in [3, 42, 999, 10, 9]:
        h1.handle(v)
