from flask import jsonify, make_response, request
from flask_restful import Resource
from werkzeug.exceptions import *


# Class responsible for /cars/
class CustomerList(Resource):
    def __init__(self, customers):
        self.customers = customers

    def get(self):
        return jsonify(self.customers.get_all())

    def post(self):
        customer = self.customers.add(request.json)

        return make_response(jsonify(customer), 201)


class Customer(Resource):
    def __init__(self, customers):
        self.customers = customers

    def get(self, id):
        customer = self.customers.get(id)

        if not customer:
            raise NotFound('Invalid customer ID, car not found')

        return jsonify(customer)

    def put(self, id):
        customer = self.customers.get(id)

        if not customer:
            raise NotFound('Invalid customer ID, car not found')

        json = request.get_json()

        customer.name = json['name']
        customer.email = json['email']
        customer.phone_number = json['phone_number']

        self.customers.update(customer)

        return jsonify(customer)

    def delete(self, id):
        customer = self.customers.get(id)

        if not customer:
            raise NotFound('Invalid car ID, car not found')

        self.customers.delete(customer)

        return jsonify(customer)
