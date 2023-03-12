#!/usr/bin/env python3
'''Defining class Amenity.'''

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Defining class Amenity inheriting from BaseModel.
    Attributes:
        name (str): name of the amenity.
    '''
    name = ""
