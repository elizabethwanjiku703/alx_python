#!/usr/bin/python3
"""Rectangle module that contains class rectangle"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init the rectangle object with given width and height"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the rectangle width"""
        if type(value) !=int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the rectangle height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the rectangle x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the rectangle x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the rectangle y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the rectangle y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width
    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)
    def __str__(self):
        """Returns a string representation of this object"""
        id_str = str(self.id)
        w_str = str(self.__width)
        h_str = str(self.__height)
        x_str = str(self.__x)
        y_str = str(self.__y)
        div_str = x_str + '/' + y_str + ' - ' + w_str + '/' + h_str
        return ("[Rectangle] " + '(' + id_str + ') ' + div_str)
    def update(self, *args, **kwargs):
        """args and kwargs"""
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
