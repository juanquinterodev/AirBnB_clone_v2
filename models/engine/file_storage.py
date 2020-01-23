#!/usr/bin/python3
"""storages class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes instances to a JSON and
    deserializes JSON to instances
    Attributes:
        __file_path: path to the JSON
        __objects: objects to be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns dictionary
        Return:
            returns dictionary of __object
        """
        if cls is None:
            return self.__objects
        else:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls.__name__ in key:
                    new_dict[key] = value
            return new_dict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects
        """
        if obj:
            key_check = ".".join([type(obj).__name__, obj.id])
            if key_check in self.__objects:
                del self.__objects[key_check]
            self.save()

    def close(self):
        """public method for deserializing JSON
        """
        self.reload()
