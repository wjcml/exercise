from abc import ABC, abstractmethod


class CarBasic(ABC):
    def __init__(self, brand):
        self.color = 'color'
        self.chair = 'chair'
        self.brand = brand

    @abstractmethod
    def build(self):
        pass


class Truck(CarBasic):
    def __init__(self, brand):
        super().__init__(brand)
        self.car_box = 'car_box'
        self.big_tire = 'big_tire'

    def build(self):
        return '卡车制造完成'


class Ambulance(CarBasic):
    def __init__(self, brand):
        super().__init__(brand)
        self.siren = 'siren'
        self.bed = 'bed'

    def build(self):
        return '救护车制造完成'


class FireTruck(CarBasic):
    def __init__(self, brand):
        super().__init__(brand)
        self.ladder = 'ladder'
        self.nozzle = 'nozzle'

    def build(self):
        return '消防车制造完成'


class Sprinkler(CarBasic):
    def __init__(self, brand):
        super().__init__(brand)
        self.water_tank = 'water_tank'

    def build(self):
        return '洒水车制造完成'
