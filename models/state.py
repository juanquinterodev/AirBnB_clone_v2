#!/usr/bin/python3
"""state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              cascade="all, delete",
                              backref="_state")
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            new = []
            my_cities = models.storage.all(City)
            for key, value in my_cities.items():
                if value.state_id == self.id:
                    new.append(value)
            return new
