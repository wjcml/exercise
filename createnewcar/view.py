from flask import request

from model import Truck, Ambulance, FireTruck, Sprinkler


car = dict()
car['1'] = Truck
car['2'] = Ambulance
car['3'] = FireTruck
car['4'] = Sprinkler


def create():
    car_type = request.form.get('car_type')
    brand = request.form.get('brand')

    car_new = Init(car_type, brand)

    return create_car(car_new)


def Init(car_type, brand):
    return car[car_type](brand)


def create_car(car_new):
    return car_new.build()