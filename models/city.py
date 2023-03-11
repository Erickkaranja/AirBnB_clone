#!/usr/bin/env python3
'''initializing class city.'''

from base_model import BaseModel

class city(BaseModel):
    '''defining class city inheriting from BaseModel.'''

    def __init__(self):
        '''constructor to class city.'''
        self.state_id = ""
        self.name = ""
