from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"[Email] {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"[SMS] {message}")


class NotifierFactory(ABC):
    @abstractmethod
    def create_notifier(self) -> Notifier:
        pass

    def notify(self, message: str):
        notifier = self.create_notifier()
        notifier.send(message)


class EmailNotifierFactory(NotifierFactory):
    def create_notifier(self) -> Notifier:
        return EmailNotifier()


class SMSNotifierFactory(NotifierFactory):
    def create_notifier(self) -> Notifier:
        return SMSNotifier()


if __name__ == "__main__":
    msg = "Событие!"
    EmailNotifierFactory().notify(msg)
    SMSNotifierFactory().notify(msg)
