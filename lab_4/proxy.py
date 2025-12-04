class Secret:
    def __init__(self, data):
        self._data = data

    def read(self):
        return self._data


class SecretProxy:
    def __init__(self, secret: Secret, has_access: bool):
        self._secret = secret
        self._has_access = has_access

    def read(self):
        if self._has_access:
            return self._secret.read()
        return "Access denied"


if __name__ == "__main__":
    real = Secret("TOP-SECRET: 42")
    proxy_no = SecretProxy(real, has_access=False)
    proxy_yes = SecretProxy(real, has_access=True)

    print(proxy_no.read())
    print(proxy_yes.read())
