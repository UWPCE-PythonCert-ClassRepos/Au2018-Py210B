#!/usr/bin/env python3

"""
Class: Python 210 B, Au2018
Exercise: Session 08, Circle Class
Student: Jason Jakubiak

A class-based system for representing a simple circle
"""

from math import pi


class Circle:

    def __init__(self, the_radius):
        if the_radius < 0:
            raise ValueError
        self.radius = the_radius

    @classmethod
    def from_diameter(cls, the_diameter):
        radius = the_diameter / 2
        return cls(radius)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return round(pi * self.radius ** 2, 6)

    def __str__(self):
        return "Circle with radius: {:0.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({:.0f})".format(self.radius)

    def __add__(self, other):
        return type(self)(self.radius + other.radius)

    def __mul__(self, value):
        return type(self)(self.radius * value)

    def __rmul__(self, value):
        return type(self)(self.radius * value)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __imul__(self, value):
        self.radius *= value
        return self

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ne__(self, other):
        return self.radius != other.radius

