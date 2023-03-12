#!/usr/bin/python3
'''Initializing class Review.'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''Defining class Review inheriting from BaseModel.
    Attributes:
        place_id (str): place id.
        user_id (str): users id.
        text (str): reviews from a user.
    '''
    place_id = ""
    user_id = ""
    text = ""
