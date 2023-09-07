#!/usr/bin/python3
class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the class"""
        if id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
