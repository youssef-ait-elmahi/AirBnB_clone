#!/usr/bin/python3
"""
The module defines the City class,
it's also is a subclass of BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for representing cities.

    Attributes:
        state_id (str): ID of the State.
        name (str): Name of the city.
    """

    state_id = ""
    name = ""
