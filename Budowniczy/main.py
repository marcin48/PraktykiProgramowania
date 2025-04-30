from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.engine = None
        self.wheels = 0

    def __str__(self):
        return f"{self.brand}, {self.model},engine size: {self.engine},wheels: {self.wheels}"


class Builder(ABC):

    def __init__(self):
        self.car = Car()

    @abstractmethod
    def set_brand(self): pass

    @abstractmethod
    def set_model(self): pass

    @abstractmethod
    def set_engine(self): pass

    @abstractmethod
    def set_wheels(self): pass

    def get_build(self):
        return self.car


class SportCarBuilder(Builder):

    def set_brand(self):
        self.car.brand = 'audi'

    def set_model(self):
        self.car.model = 'R8'

    def set_engine(self):
        self.car.engine = '5.0L'

    def set_wheels(self):
        self.car.wheels = 4


class Director:
    def __init__(self, builder: Builder):
        self._builder = builder

    def build_car(self):
        self._builder.set_brand()
        self._builder.set_model()
        self._builder.set_engine()
        self._builder.set_wheels()
        return self._builder.get_build()


sportCar = SportCarBuilder()
director = Director(sportCar)
car = director.build_car()
print(car)
