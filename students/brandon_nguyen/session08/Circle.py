#!/usr/bin/env python3
# Week8 Excercise circle.py
# Student: Brandon Nguyen - Au2018

from math import pi


class Circle(object):

    def __init__(self, radius):
        # check radius error r !<= 0
        if radius <= 0:
            raise ValueError("Radius is defined to be greater than 0!")
        # self.radius = radius  # let use @property instead
        self.__radius = radius
        self.__diameter = radius * 2

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    # now we can reset the radius & diameter
    def radius(self, r):
        self.__radius = r
        self.__diameter = r*2

    @property
    def diameter(self):
        return self.__diameter
    
    @diameter.setter
    def diameter(self, d):
        self.__radius = d/2

    @property
    def area(self):
        return pi * (self.__radius**2)

    @classmethod
    def from_diameter(cls, d_value):
        return cls(d_value/2)

    def __str__(self):
        return "Circle with radius: {}".format(self.__radius)

    def __repr__(self):
        return "Circle({})".format(self.__radius)

    def __add__(self, other):
        return type(self)(self.__radius + other.radius)

    def __mul__(self, r):
        return type(self)(self.__radius * r)
