#!/usr/bin/python3
'''initializing class city.'''

from  models.base_model import BaseModel


class City(BaseModel):
    '''defining class city inheriting from BaseModel.
    Attributes:
        state_id (str): state's id.
        name (str): Name of the state.
    '''
    state_id = ""
    name = ""
