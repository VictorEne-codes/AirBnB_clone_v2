#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ Te State class"""
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """returns the list of City instances with state_id"""
            from models import storage
            rel_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    rel_cities.append(city)
            return rel_cities
