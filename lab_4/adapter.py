class LegacyThermometer:
    def read_fahrenheit(self) -> float:
        return 86.0


class Thermometer:
    def read_celsius(self) -> float:
        raise NotImplementedError


class ThermometerAdapter(Thermometer):
    def __init__(self, legacy: LegacyThermometer):
        self._legacy = legacy

    def read_celsius(self) -> float:
        f = self._legacy.read_fahrenheit()
        return (f - 32) * 5.0 / 9.0


if __name__ == "__main__":
    legacy = LegacyThermometer()
    adapter = ThermometerAdapter(legacy)
    print(f"{adapter.read_celsius():.1f} C")
