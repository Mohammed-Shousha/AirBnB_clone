#!/usr/bin/python3
"""BaseModel class module"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    BaseModel class
    Attributes:
        id (str): id of the instance
        created_at (datetime): time of creation
        updated_at (datetime): time of update
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        to_dict(self)
    """

    def __init__(self):
        """Initializes the instance"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """Updates the instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dictionary representation of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict