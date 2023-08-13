#!/usr/bin/python3
"""
The module defines the Amenity class,
it's also is a subclass of BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for representing amenities.

    Attributes:
        name (str): Name of amenity.
    """

    name = ""
