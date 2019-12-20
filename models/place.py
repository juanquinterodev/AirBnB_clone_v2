#!/usr/bin/python3
"""This is the place class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy import ForeignKey
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    metadata = Base.metadata
    place_amenity = Table("place_amenity", metadata,
                            Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
                            Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False))

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenity_ids = []
    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

    else:
    
        @property
        def amenities(self):
            """
            amenety list with append method
            :return: list of amenity instances
            """
            amenity_list = []
            results = models.storage.all(Amenity)
            for amenity in results.values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """
            :param obj: ppends place id for amenities
            """
            if obj and isinstance(obj, Amenity):
                type(self).amenity_ids.append(obj.id)
        

    @property
    def reviews(self):
        """
        Getter attribute reviews
        :return: the list of reviews
        """
        review_dict = {}
        objs_ = models.storage.all(Review)
        for key, value in objs_.items():
            if value.place_id == self.id:
                review_dict[key] = value
        return review_dict
