#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """
    Defines a class rectangle with private attribute width and height


    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        """
        def __init__(self, width=0, height=0):
            """Initializes rectangles"""
            self.width = width
            self.height = height

        @property
        def width(self, value):
            """Getter returns width"""
            return self.__width

        @width.setter
        def width(self, value):
            """Setter sets width if int > 0"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Retriever returns height."""
            return self.__height

        @height.setter
        def height(self, value)
            """Setter sets height if int > 0"""
            if not isinstance(value, int):
                raise TypeError("height has to be an integer")

