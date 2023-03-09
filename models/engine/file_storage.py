#!/usr/bin/env python3
'''initializes class filestorage'''

import json
from models.base_model import BaseModel


class FileStorage:
    '''declaring class file storage.'''

    def __init__(self):
        '''constructor to class file storage.
        Attributes:
        __file_path(str): The name of the file to save objects to.
        __objects(dict): A dictionary of objects.
        '''
    __file_path = "file.json"
    __objects = {}
    def all(self):
        '''returns the dict object.'''

        return (self.__objects)

    def new(self, obj):
        '''sets objects with keys <obj class name>.id.'''

        self.__objects[{}.{}.format(type(obj).__name__, obj.id)] = obj

    def save(self):
        '''serializes __objects to the JSON file.'''

        json_string = json.dumps(self.__objects)
        with open(self.__file_path, "w") as jsonfile:
            jsonfile.write(json_string)

    def reload(self):
        ''' deserializes the JSON file to __objects.'''
        if self.__file_path is != 0:
            with open(self.__file_path, "r") as obj:
                obj_new = obj.loads(obj)
        return obj_new
