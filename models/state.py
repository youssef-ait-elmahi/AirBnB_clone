#!/usr/bin/python3
"""
The module defines the City class,
it's also is a subclass of BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
