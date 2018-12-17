#!/usr/bin/env python3

##################################################
# Author: Jackie Cheung
# Date: 2018/12/04
# Version: 0.1
# Class: Au2018-Py210B
# Description: The Circle Class - Unit Testing
##################################################

import pytest
import math
from circle import Circle
from circle import Sphere

# Tests if new Circle created with corresponding radius
def test_circle_init():
    c = Circle(2)
    assert c.radius == 2
    assert c.diameter == 2 * 2
    assert c.area == math.pi * 2 ** 2


# Tests if string method is working for Circle
def test_circle_str():
    assert str(Circle(4)) == 'Circle with radius: 4'


def test_circle_add():
    assert Circle(2) + Circle(4) == Circle(6)


def test_circle_iadd():
    assert Circle(2) + Circle(4) == Circle(6)


def test_circle_radd():
    assert Circle(2) + Circle(4) == Circle(6)


def test_circle_mul():
    assert Circle(4) * 3 == Circle(12)


def test_circle_imul():
    assert Circle(4) * 3 == Circle(12)


def test_circle_rmul():
    assert Circle(4) * 3 == Circle(12)


'''
Tests if the circle comparisions are working
'''

def test_circle_gt():
    assert Circle(4) > Circle(2)


def test_circle_lt():
    assert Circle(2) < Circle(4)


def test_circle_eq():
    assert Circle(2) == Circle(4/2)
    assert Circle(2) != Circle(3)


# Tests if new Sphere created with corresponding radius
def test_sphere_init():
    s = Sphere(2)
    assert s.area == math.pi * 2 ** 2 * 4
    assert s.volume == math.pi * 2 ** 3 * 4/3


# Tests if string method is working for Sphere
def test_sphere_str():
    assert str(Sphere(4)) == 'Sphere with radius: 4'