#!/usr/bin/python3
""" Base module contains class Base """

class Base:
    """Base class for all classes"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instance class base id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
