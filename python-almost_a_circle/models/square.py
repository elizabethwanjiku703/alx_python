""" Rectangle model """

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square with a given size"""
        super(). __init__(size, size, x, y, id)
    
    @property
    def size(self):
        """Returns the size of the square"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value
    
    def __str__(self):
        """ Returns a string representation of the square"""
        id_str = str(self.id)
        w_str = str(self.width)
        x_str = str(self.x)
        y_str = str(self.y)
        div_str = x_str + '/' + y_str + ' - ' + w_str
        return ("[Square] " + '(' + id_str + ') ' + div_str)
