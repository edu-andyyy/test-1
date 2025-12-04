class SingletonLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, prefix="LOG"):
        if getattr(self, "_initialized", False):
            return
        self.prefix = prefix
        self.logs = []
        self._initialized = True

    def log(self, message):
        entry = f"{self.prefix}: {message}"
        self.logs.append(entry)
        print(entry)

    def get_logs(self):
        return list(self.logs)


if __name__ == "__main__":
    a = SingletonLogger("APP")
    b = SingletonLogger("OTHER")  # не создаст новый объект и не перезапишет prefix

    print(a is b)  # True

    a.log("started")  # APP: started
    b.log("working")  # APP: working

    print(a.get_logs())  # ['APP: started', 'APP: working']
