#!/usr/bin/env python3
'''Defining class Amenity.'''

from bas_model import BaseModel

class Amenity(BaseModel):
    '''Defining class Amenity inhetiting from BaseModel.'''

    def __init__(self):
        '''Constructor to class Amenity.'''
        self.name = ""
