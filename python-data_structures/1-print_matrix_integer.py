#Write a function that prints a matrix of integers.
#Prototype: def print_matrix_integer(matrix=[[]]):
#Format: see example
#You are not allowed to import any module
#You can assume that the list only contains integers
#You are not allowed to cast integers into strings
#You have to use str.format() to print integers

def print_matrix_integer(matrix=[]):
    for row in matrix:
        for i, element in enumerate(row):
            print("{:d}".format(element), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print() # Move this print() outside of the inner loop
