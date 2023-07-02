from flask import jsonify, make_response, request
from flask_restful import Resource
from werkzeug.exceptions import *


# Class responsible for /cars/
class CarList(Resource):
    def __init__(self, cars):
        self.cars = cars

    def get(self):
        return jsonify(self.cars.get_all())

    def post(self):
        car = self.cars.add(request.json)

        return make_response(jsonify(car), 201)


class Car(Resource):
    def __init__(self, cars):
        self.cars = cars

    def get(self, id):
        car = self.cars.get(id)

        if not car:
            raise NotFound('Invalid car ID, car not found')

        return jsonify(car)

    def put(self, id):
        car = self.cars.get(id)

        if not car:
            raise NotFound('Invalid car ID, car not found')

        json = request.get_json()

        car.brand = json['brand']
        car.model = json['model']
        car.year_model = json['year_model']
        car.color = json['color']
        car.customer_id = json['customer_id']
        self.cars.update(car)

        return jsonify(car)

    def delete(self, id):
        car = self.cars.get(id)

        if not car:
            raise NotFound('Invalid car ID, car not found')

        self.cars.delete(car)

        return jsonify(car)
