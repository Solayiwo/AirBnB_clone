#!/usr/bin/python3
"""
FileStorage module
Defines the FileStorage class to manage serialization
and deserialization of instances.
"""


import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                obj_dict = json.load(json_file)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    models_dict = {'BaseModel': BaseModel, 'User': User,
                                   'State': State, 'Place': Place,
                                   'City': City, 'Amenity': Amenity,
                                   'Review': Review}
                    if cls_name in models_dict.keys():
                        self.__objects[key] = models_dict[cls_name](**value)
