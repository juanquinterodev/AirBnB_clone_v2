#!/usr/bin/python3
""" Engine for Database Storage """

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel, Base
from os import getenv

class DBStorage:
    """
    Class for Database Storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize an instance
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        query on the current database session all objects depending of the class name
        """
        if cls is None:
               types = self.__session.query(City, State, User, Place,
                                           Review).all()
        else:
            types = self.__session.query(cls).all()
        type_dict = {}
        for row in types:
            key = ".".join([type(row).__name__, row.id])
            type_dict[key] = row
        return type_dict
    
    def new(self, obj):
        """
        Add the object to the current database session
        """
        if obj:
            self.__session.add(obj)
    
    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()
    
    def delete(self, obj=None):
        """
        Delete from the current database session
        """
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """
        Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
    
    def close(self):
        """ Closes session """
        self.__session.remove()
