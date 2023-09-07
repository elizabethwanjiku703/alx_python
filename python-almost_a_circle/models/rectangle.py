#!/usr/bin/python3

"""Rectangle module that contains class rectangle"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """init the rectangle object with given width and height"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for the rectangle width"""
        self.__width = width

    @property
    def height(self):
        """Getter for the rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for the rectangle height"""
        self.__height = height

    @property
    def x(self):
        """Getter for the rectangle x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for the rectangle x"""
        self.__x = x

    @property
    def y(self):
        """Getter for the rectangle y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for the rectangle y"""
        self.__y = y

