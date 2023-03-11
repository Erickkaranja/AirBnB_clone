#!/usr/bin/env python3
'''Defining class BaseModel.'''

import uuid
from datetime import datetime
from __init__ import storage


class BaseModel:
    '''initializing class basemodel.'''

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or "upadated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        '''prints the class name, id and dict representation of object.'''
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute updated_at with the current
            datetime.'''
        updated_at = datetime.utcnow()
        save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values.'''
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
