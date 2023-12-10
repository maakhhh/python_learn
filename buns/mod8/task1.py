class Transport():
    def __init__(self, *args, **kwargs):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        '''
           Представление всей информации для вывода в методе print()
        '''
        pass

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        pass


class Passenger():
    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        pass

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        pass


class Cargo():
    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        pass


class Plane(Transport):
    def __init__(self, *args, **kwargs):
        self.height = height


class Auto(Transport):
    def __init__(self, *args, **kwargs):


class Ship(Transport):
    def __init__(self, name, *args, **kwargs):
        self.port = port


class Car(Auto):
    class Bus(Auto, Passenger):

        class CargoAuto(Auto, Cargo)


class Boat(Ship):
    class PassengerShip(Ship, Passenger):

        class CargoShip(Ship, Cargo):
