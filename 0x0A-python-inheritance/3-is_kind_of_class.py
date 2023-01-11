#!/usr/bin/python3
"""Defines a class and inherited classs-checking function."""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class.

    Args:
        obj (any): The object to check
        a_class (type): the class to match the type of obj to.
    Returns:
        If an obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
        """
    if isinstance(obj, a_class):
        return True
    return False
