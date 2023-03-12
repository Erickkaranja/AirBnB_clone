#!/usr/bin/python3
'''initializing class Place.'''

from models.base_model import BaseModel


class Place(BaseModel):
    '''Defining class Place inheriting from BaseModel.

    Attributes:
        city_id (str): city id.
        user_id (str): user id.
        name (str): Name of the place.
        description (str): Desription of the place.
        number_room (int): Number of rooms.
        number_bathrooms (int): Number of bathrooms.
         max_guest (int): The number of maximum guests.
        price_by_night (int): price of the place.
        latitude (float): latitude location.
        longitude (float): longitude location.
        amenity_ids (list): list of amenities per id.
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
