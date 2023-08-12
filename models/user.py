#!/usr/bin/python3
"""This Initializes the User class."""
from models.base_model import BaseModel

class User(BaseModel):
	"""This constitutes a user.
	Attr:
		first_name: User first name.
		last_name: User last name.
		email: User email.
		password: User password.
	"""

	first_name = ""
	last_name = ""
	email = ""
	password = ""

