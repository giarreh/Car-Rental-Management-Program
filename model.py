from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@dataclass
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(Integer)
    # Creates relationship between customer and car
    cars = relationship('Car', back_populates='customer')

    # Types for each index or column
    id: int
    name: str
    email: str
    phone_number: int


@dataclass
class Car(Base):
    # Class for each car
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    year_model = Column(Integer)
    color = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    # Creates relationship between customer and car

    customer = relationship('Customer', back_populates='cars')

    # Types for each index or column
    id: int
    brand: str
    model: str
    year_model: int
    color: str
    customer_id: int

