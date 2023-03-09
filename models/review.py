#!/usr/bin/env python3
'''Initializing class Review.'''

from base_model import BaseModel

class Review(BaseModel):
    '''Defining class Review inheriting from BaseModel.'''

    def __init__(self):
        '''Constructor to class Review.'''
        self.place_id = ""
        self.user_id = ""
        self.text = ""
