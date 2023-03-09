#!/usr/bin/env python3
'''initializing class user.'''

from base_model import BaseMode

class User(BaseModel):
    '''defining class user that inherits from BaseModel.'''

    def __init__(self):
        '''constructor to class user.'''
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
