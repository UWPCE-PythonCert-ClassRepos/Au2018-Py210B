#!/usr/bin/env python3

##################################################
# Author: Jackie Cheung
# Date: 2018/12/04
# Version: 0.1
# Class: Au2018-Py210B
# Description: The Circle Class - Properties and Magic Methods
##################################################

import random
import time
import math

class Circle:
    
    def __init__(self, radius):
        self._radius = radius

    # Step 1 - circle with radius
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("radius cannot be less than zero")
        self._radius = new_radius

    # Step 2 - diameter
    @property
    def diameter(self):
        return self.radius * 2
    
    # Step 3 - set diameter
    @diameter.setter
    def diameter(self, new_diameter):
        self.radius = new_diameter / 2

    # Step 4 - area
    @property
    def area(self):
        # return self._radius * self._radius * math.pi
        return self._radius ** 2 * math.pi

    # Step 5 - alternate constructor
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    # Step 6 - __str__ and __repr__
    def __str__(self):
        return "Circle with radius: " + str(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    # Step 7 - adding circle
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        return Circle(self.radius + other.radius)

    def __radd__(self, other):
        return Circle(self.radius + other.radius)

    # Step 8 - optional feature
    def __mul__(self, other):
        return Circle(self.radius * other)

    def __imul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    # Step 8 - comparing circle
    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    @staticmethod
    def sort_by_raidus(self):
        return self.radius

# Step 9 - subclassing
class Sphere(Circle):

    @property
    def volume(self):  # 4/3 pi r^3
        # return super().radius * super().radius * super().radius * math.pi * 4 / 3
        return super().radius ** 3 * math.pi * 4 / 3

    @property
    def area(self):  # 4 pi r^2
        # return 4 * math.pi * super().radius * super().radius
        return 4 * math.pi * super().radius ** 2

    def __str__(self):
        return "Sphere with radius: " + str(super().radius)

    def __repr__(self):
        return "Sphere({})".format(super().radius)