"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from homework_05.exceptions import CargoOverload
class Plane(Vehicle):
    def __init__(self, weight, fuel, max_cargo):
        super().__init__(weight, fuel)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, value):
        if self.cargo + value <= self.max_cargo:
            self.cargo += value
        else:
            raise CargoOverload("Превышена максимальная грузоподъемность!")

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo
