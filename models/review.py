#!/usr/bin/python3
"""
This module defines the Review class.
it's also is a subclass of BaseModel.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Attributes:
        place_id (str): The associated Place's ID.
        user_id (str): The associated User's ID.
        text (str): The review text.
    """

    place_id = ""
    user_id = ""
    text = ""
