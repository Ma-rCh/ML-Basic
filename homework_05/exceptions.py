"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self, messege="Недостаточно топлива!"):
        self.messege = messege
        super().__init__(self.messege)


class NotEnoughFuel(LowFuelError):
   pass

class CargoOverload(Exception):
    def __init__(self, messege):
        self.messege = messege
        super().__init__(self.messege)
