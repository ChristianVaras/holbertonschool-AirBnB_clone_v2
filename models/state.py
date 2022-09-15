#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            new_list = []
            cities_all = models.storage.all(City)
            for value in cities_all.values():
                if (value.state_id == self.id):
                    new_list.append(value)
            return new_list
