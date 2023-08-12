from datetime import datetime
import models
import uuid


class BaseModel:
    """
    Represents a base model with common attributes and methods.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            args: Variable length arguments.
            kwargs: Keyword arguments.

        Attributes:
            id (str): The unique identifier of the BaseModel instance.
            created_at (datetime): The timestamp of when the BaseModel
            instance was created.
            updated_at (datetime): The timestamp of when the BaseModel
            instance was last updated.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute and saves the BaseModel instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.
        """
        tmp = {}
        d = self.__dict__
        d["__class__"] = self.__class__.__name__
        for key, value in d.items():
            if key == "created_at" or key == "updated_at":
                tmp[key] = value.isoformat()
            else:
                tmp[key] = value
        return tmp
