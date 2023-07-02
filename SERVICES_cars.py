# Class used to access authors data using a session

from model import Car


class CarService:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.session.query(Car).all()

    def get(self, id):
        return self.db.session.query(Car).get(id)

    def add(self, json):
        car = Car(brand=json['brand'], model=json['model'], year_model=json['year_model'], color=json['color'], customer_id=json['customer_id'])

        self.db.session.add(car)
        self.db.session.commit()

        return car

    def update(self, car):
        self.db.session.commit()

    def delete(self, car):
        self.db.session.delete(car)
        self.db.session.commit()
