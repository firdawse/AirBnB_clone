#!/usr/bin/python3
'''This is a AirBnB clone project File Storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ This is the storage engine for AirBnB clone project
    Class Methods:
        all: Returns all the object
        new: updates the dictionary id to the new one.
        save: Converts Python objects into JSON strings (sterilizes)
        reload: Converts JSON strings into Python objects (Desterilizes).
    Class Attributes:
        __file_path (str): Thi is the name of the file path to be saved to.
        __objects (dict): This is a dictionary instantiated to the value pair
        present in it.
        class_dict (dict): This is the dictionary of all the  classes present
        or available.
    """

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}
    def all(self):
        '''Return dictionary of <class id>:object instance'''
        return self.__objects

    def new(self, ob):
        '''Set new __objects to existing dictionary of instances'''
        if ob:
            key = '{}.{}'.format(ob.__class__.__name__, ob.id)
            self.__objects[key] = ob

    def save(self):
        """This saves object to json file"""
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize/convert obj dicts back to instances when exits"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
