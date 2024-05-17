#!/usr/bin/python3
"""
FileStorage module
Defines the FileStorage class to manage serialization
and deserialization of instances.
"""


import os
import json
from models.base_model import BaseModel


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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file exists)."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                obj_dict = json.load(json_file)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
