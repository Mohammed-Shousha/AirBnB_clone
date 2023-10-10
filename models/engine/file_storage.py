#!/usr/bin/python3
"""FileStorage class module"""

import json
import os


class FileStorage():
    """
    FileStorage class
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    Methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initializes the instance"""
        pass

    def all(self):
        """Returns the dictionary representation of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as file:
            storage_dict = {k: v.to_dict()
                            for k, v in FileStorage.__objects.items()}
            json.dump(storage_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r") as file:
            strorage_dict = json.load(file)
            for v in strorage_dict.values():
                cls = v["__class__"]
                self.new(eval(cls)(**v))
