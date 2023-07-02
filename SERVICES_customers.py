from model import Customer


class CustomerService:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.session.query(Customer).all()

    def get(self, id):
        return self.db.session.query(Customer).get(id)

    def add(self, json):
        customer = Customer(name=json['name'], email=json['email'], phone_number=json['phone_number'])

        self.db.session.add(customer)
        self.db.session.commit()

        return customer

    def update(self, customer):
        self.db.session.commit()

    def delete(self, customer):
        self.db.session.delete(customer)
        self.db.session.commit()
