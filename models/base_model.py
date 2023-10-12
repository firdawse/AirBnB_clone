#!/usr/bin/python3
"""
Our Base Module
"""

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        - Sets a unique 'id' using UUID.
        - Sets 'created_at' to the current datetime.
        - Sets 'updated_at' to 'created_at' initially.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute to the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the object to a dictionary.
        - Adds '__class__' key with the class name.
        - Formats 'created_at' and 'updated_at' as ISO strings.
        """
        class_name = type(self).__name__
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = class_name
        return obj_dict

