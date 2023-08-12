#!/usr/bin/python3
"""
This module defines the User class, which inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class represents a user and extends the BaseModel class.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
