#!/usr/bin/python3
"""Define the City class"""

from models.basemodel import BaseModel


class City(BaseModel):
    """
        - City class that inherits from BaseModel
        - To manage the public class attributes
            - state_id
            - name(city)
    """

    state_id = ""
    name = ""
