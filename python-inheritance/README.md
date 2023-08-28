# Python - Inheritance
|Tasks|	Description|
|-----|------------|
|0. Exact same object |Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.|
|1. Same class or inherit from|Write a function that returns True if the object is an instance of or if the object is<br /> an instance of a class that inherited from, the specified class ; otherwise False.|
|2. Only sub class of |Write a function that returns True if the object is an instance of a class that inherited<br /> (directly or indirectly) from the specified class ; otherwise False.|
|3. Geometry module |Write an empty class BaseGeometry.|
|4. Improve Geometry|Write a class BaseGeometry (based on 3-base_geometry.py).Public instance method: def area(self):<br /> that raises an Exception with the message area() is not implemented|
|5. Integer validator|Write a class BaseGeometry (based on 4-base_geometry.py).Public instance method: def area(self):<br /> that raises an Exception with the message area() is not implemented Public instance method: def integer_validator(self, name, value): that validates value:<br /> you can assume name is always a string if value is not an integer: raise a TypeError exception, with the message <name> must be an integer<br /> if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0|
|6. Rectangle |Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).<br /> Instantiation with width and height: def __init__(self, width, height):<br /> width and height must be private. No getter or setter <br /> width and height must be positive integers, validated by integer_validator|
|7. Full rectangle |Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py). (task based on 6-rectangle.py)<br /> Instantiation with width and height: def __init__(self, width, height)::<br /> width and height must be private. No getter or setter. <br /> width and height must be positive integers validated by integer_validator|
|8. Square #1|Write a class Square that inherits from Rectangle (7-rectangle.py):<br /> Instantiation with size: def __init__(self, size):: <br /> size must be private. No getter or setter<br /> size must be a positive integer, validated by integer_validator <br /> the area() method must be implemented.|






