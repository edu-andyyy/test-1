class Sender:
    def send(self, text: str):
        raise NotImplementedError


class EmailSender(Sender):
    def send(self, text: str):
        print(f"[Email] {text}")


class SmsSender(Sender):
    def send(self, text: str):
        print(f"[SMS] {text}")


class Message:
    def __init__(self, sender: Sender):
        self._sender = sender

    def send(self, text: str):
        self._sender.send(text)


class NormalMessage(Message):
    def send(self, text: str):
        super().send(text)


class UrgentMessage(Message):
    def send(self, text: str):
        urgent_text = f"URGENT: {text}"
        self._sender.send(urgent_text)
        self._sender.send(f"{urgent_text} (repeat)")


if __name__ == "__main__":
    email = EmailSender()
    sms = SmsSender()

    m1 = NormalMessage(email)
    m2 = UrgentMessage(sms)

    m1.send("Событие!")
    m2.send("Server is down!")
