#!/usr/bin/python3
"""This initiates the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Constitutes a review.
    Attrs:
        place_id: Place ID.
        user_id: User ID.
        text: text of review.
    """

    place_id = ""
    user_id = ""
    text = ""
