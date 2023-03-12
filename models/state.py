#!/usr/bin/python3
'''initializes class state.'''

from models.base_model import BaseModel


class State(BaseModel):
    '''Defing class statethat inherits from BaseModel.
    Attributes:
        name (str): Name of the state.
    '''
    name = ""
