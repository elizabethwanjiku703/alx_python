#!/usr/bin/env python3
#Write a function that removes all characters c and C from a string.
# Prototype: def no_c(my_string):
# The function should return the new string
# You are not allowed to import any module
# You are not allowed to use str.replace()

def no_c(my_string):
    new_string = ''
    for letter in my_string:
        if letter != "c" and letter != "C":
            new_string += letter
    return new_string

