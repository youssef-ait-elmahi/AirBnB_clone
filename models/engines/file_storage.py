import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        d = {}
        for key, obj in FileStorage.__objects.items():
            d[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(d, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                d = json.load(f)
            for key, obj_dict in d.items():
                class_name = obj_dict["__class__"]
                if class_name == "BaseModel":
                    obj = BaseModel()
                    obj.__dict__.update(obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
