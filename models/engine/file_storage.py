#!/usr/bin/python3
"""
FileStorage class for storing and retrieving objects.
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
}


class FileStorage:
    """
    This class represents a file storage system for storing
    and retrieving objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve and access to the stored objects (__objects)
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize and store __objects as JSON in
        the designated file (__file_path).
        """
        data = {}

        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        file_path = FileStorage.__file_path

        if not os.path.isfile(file_path):
            return

        with open(file_path, "r") as f:
            data = json.load(f)

        FileStorage.__objects = {}
        for k, v in data.items():
            name = k.split(".")[0]
            FileStorage.__objects[k] = classes[name](**v)

        return FileStorage.__objects
