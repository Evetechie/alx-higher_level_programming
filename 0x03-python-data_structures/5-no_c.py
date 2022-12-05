#!/usr/bin/env python3
def no_c(my_string):
    new_string = my_string[:]
    return ("".join (char for char in copy if char not in "cC")
