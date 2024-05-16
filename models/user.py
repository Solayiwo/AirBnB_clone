#!/usr/bin/python3
"""Define the User class"""

from models.basemodel import BaseModel


class User(BaseModel):
    """
    User class which inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
