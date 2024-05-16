#!/usr/bin/python3
"""Define the State class"""

from models.basemodel import BaseModel


class State(BaseModel):
    """
        - State class that inherits from BaseModel
        - To manage the public class attributes(name)
    """

    name = ""
