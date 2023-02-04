#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (Int): The width of the new rectangle.
            height (Int): The height of the new rectangle .
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width attribute of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width has to be an integer")
        if value < 0:
            raise ValueError("width has to be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the height attribute of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height has to be an integer")
        if value < 0:
            raise ValueError("height has to be >= 0")
        self.__height = value

        def area(self):
            """Return the area of the Rectangle."""
            return (self.__width * self.__height)

        def perimeter(self):
            """Return the perimeter of the rectangle."""
            if self.__width == 0 or self.__height == 0:
                return (0)
            return ((self.__width * 2) * (self.__height * 2))
