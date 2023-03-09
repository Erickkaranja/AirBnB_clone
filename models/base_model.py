#!/usr/bin/env python3
'''Defining class BaseModel.'''

import storage
import uuid
from datetime import datetime


class BaseModel:
    '''initializing class basemodel.'''

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''prints the class name, id and dict representation of object.'''
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute updated_at with the current
            datetime.'''
        updated_at = datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys/values.'''
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
