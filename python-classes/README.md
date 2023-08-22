#Pyhton Objects and Classes

|          Tasks			 |                                           Description                                    |
|---------------------------------------------------------------------------|-------------------------------------------------------|
|0. Square with size | Write a class Square that defines a square by:
                        a. Private instance attribute: size
                        b. Instantiation with size (no type/value verification)
                        c. You are not allowed to import any module                                                                 |
|1. Size validation  |Write a class Square that defines a square by: (based on 0-square.py)
                       . Private instance attribute: size
                       . Instantiation with optional size: def __init__(self, size=0):
                         a. size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
                         b. if size is less than 0, raise a ValueError exception with the message size must be >= 0                 |
|2. Area of a square |Write a class Square that defines a square by: (based on 1-square.py)
                       . Private instance attribute: size
                       . Instantiation with optional size: def __init__(self, size=0):
                        a.  size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
                        b.  if size is less than 0, raise a ValueError exception with the message size must be >= 0
                       . Public instance method: def area(self): that returns the current square area                                |
|3. Access and update
 private attribute   |Write a class Square that defines a square by: (based on 2-square.py)
                       . Private instance attribute: size:
                       . property def size(self): to retrieve it
                         property setter def size(self, value): to set it:
                        a. size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
                        b. if size is less than 0, raise a ValueError exception with the message size must be >= 0
                       . Instantiation with optional size: def __init__(self, size=0):
                       .Public instance method: def area(self): that returns the current square area                                 |
|4. Printing a square|Write a class Square that defines a square by: (based on 3-square.py)
                      . Private instance attribute: size:
                      . property def size(self): to retrieve it
                      . property setter def size(self, value): to set it:
                        a. size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
                        b. if size is less than 0, raise a ValueError exception with the message size must be >= 0
                      . Instantiation with optional size: def __init__(self, size=0):
                      . Public instance method: def area(self): that returns the current square area
                      . Public instance method: def my_print(self): that prints in stdout the square with the character #:
                        a. if size is equal to 0, print an empty line                                                                |

