#!/usr/bin/python3
"""Base class for all classes"""
class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance of the class with the given id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
