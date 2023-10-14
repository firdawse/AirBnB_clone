#!/usr/bin/python3
"""user class, subclass of BaseModel
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''Derived class of Basemodel class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
