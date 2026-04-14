
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, weight, fuel, started=False, fuel_consumption=10):
        self._weight = weight
        self._fuel = fuel
        self._started = started
        self._fuel_consumption = fuel_consumption

    @property
    def weight(self):
        return self._weight
    @property
    def fuel(self):
        return self._fuel

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @weight.setter
    def weight(self, value):
            self._weight = value

    @fuel.setter
    def fuel(self, value):
            self._fuel = value

    @fuel_consumption.setter
    def fuel_consumption(self, value):
            self._fuel_consumption = value

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def move(self, distance):
        pass


#v1 = Vehicle(weight=5, fuel=10)
#v1.start(1)