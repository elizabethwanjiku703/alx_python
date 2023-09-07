#!/usr/bin/python3
"""Base class for all classes"""
class Base:
    __nb_objects = 0

    def __init__(self, id=None):
<<<<<<< HEAD
        """Initializes a new instance of the class with the given id"""
=======
        """Initialize a new instance of the class"""
>>>>>>> c3e5fb9be8eeeca9d04573745dbd8fa810c1b7e7
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
