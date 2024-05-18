#!/usr/bin/python3
"""
Module review
Defines class Review
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class definition"""

    place_id = ""
    user_id = ""
    text = ""
