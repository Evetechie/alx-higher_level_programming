#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represents a Rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height  (int): The height of the new rectangle.
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width has to  be an integer")
        if value < 0:
            raise ValueError("width has to  be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height has to be an integer")
        if value < 0:
            raise ValueError("height has to be >= 0")
        self.__height = value
