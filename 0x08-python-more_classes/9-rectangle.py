#!/usr/bin/python3
'''
    This module has a class named Rectangle
'''


class Rectangle:
    '''
        Class named Rectangle
        Attributes:
            __width : private instance attribute
            __height : private instance attribute
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''
        Attributes:
            width : private instance attribute
            height : private instance attribute

        Raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
                TypeError: height must be an integer
                ValueError: height must be >= 0
        '''
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''
            retriver for the width attribute
            Returns: the width
        '''
        return self.__width

    @property
    def height(self):
        '''
            retriver for the height attribute
            Returns: the height
        '''
        return self.__height

    @width.setter
    def width(self, value):
        '''
            setter for the width attribute
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''
            setter for the height attribute
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
            Returns: the rectangle area
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
            Returns: The rectangle perimeter
        '''
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2

    def __str__(self):
        '''
            str method reprensent the class rectangle as printable objec
        '''
        width = self.__width
        height = self.__height
        result = ""

        if width == 0 or height == 0:
            return ""
        for i in range(height):
            for j in range(width):
                result += str(self.print_symbol)
            result += "\n"
        return result.rstrip("\n")

    def __repr__(self):
        '''
            repr method reprensent the class rectangle as printable objec
        '''
        width = self.__width
        height = self.__height
        return f"Rectangle({width}, {height})"

    def __del__(self):
        '''
            print the message "Bye rectangle..." when an instance of Rectangle
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
