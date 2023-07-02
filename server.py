import flask.scaffold

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from SERVICES_cars import CarService
from CONTROLLER_cars import Car, CarList

from SERVICES_customers import CustomerService
from CONTROLLER_customers import Customer, CustomerList


def main():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'

    api = Api(app)
    db = SQLAlchemy(app)

    cars = CarService(db)
    customers = CustomerService(db)

    api.add_resource(CarList, '/cars/', resource_class_args=[cars])
    api.add_resource(Car, '/cars/<id>', resource_class_args=[cars])
    api.add_resource(CustomerList, '/customers/', resource_class_args=[customers])
    api.add_resource(Customer, '/customers/<id>', resource_class_args=[customers])
    
    app.run(debug=True)


if __name__ == '__main__':
   main()
