#!/usr/bin/python3
'''initializes class filestorage'''

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''declaring class file storage.
    Attributes:
    __file_path(str): The name of the file to save objects to.
    __objects(dict): A dictionary of objects.
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dict object.'''

        return FileStorage.__objects

    def new(self, obj):
        '''sets objects with keys <obj class name>.id.'''

        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        '''serializes __objects to the JSON file.'''

        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        ''' deserializes the JSON file to __objects.'''
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))

        except FileNotFoundError:
            return
