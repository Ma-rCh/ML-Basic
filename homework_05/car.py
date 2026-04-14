"""
Создайте класс `Car`, наследник `Vehicle`
"""

from exceptions import LowFuelError,NotEnoughFuel
from base import Vehicle
from engine import Engine

class Car(Vehicle):
    def __init__(self, weight, fuel):
        super().__init__(weight, fuel)
        #self.engine = engine

    def set_engine(self, engine):
        self.engine = engine
    #@property
    def start(self):

        if not self._started:
            if self._fuel_consumption == 0:
                raise LowFuelError()
            else:
                self._started = True
    #@property
    def move(self, distance):
        if self._started:
            if distance > self._fuel / self._fuel_consumption:
                raise NotEnoughFuel()
            else:
                self._fuel -= distance * self._fuel_consumption
                print(f"Поехали! \nОстаток топлива к финишу:  {self._fuel} литров.")


e1 = Engine(50)
c1 = Car(10,100)
c1.set_engine(e1)
print(c1.engine)
print(c1.fuel)
print(c1.weight)
try:
    c1.start
    c1.move(10)
except LowFuelError as e:
    print(f"Ошибка : {e}")