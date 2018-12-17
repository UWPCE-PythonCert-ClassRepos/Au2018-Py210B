#!/usr/bin/env python3

"""
Class: Python 210 B, Au2018
Exercise: Session 08, Circle Class Test
Student: Jason Jakubiak

Unit tests for Circle Class exercise
"""

from circle_class import *
import pytest

def test_step01():
    c = Circle(4)
    assert c.radius == 4


def test_step02():
    c = Circle(4)
    assert c.diameter == 8


def test_step03():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1


def test_step04():
    c = Circle(2)
    assert round(c.area,5) == 12.566370
    with pytest.raises(AttributeError):
        c.area = 12


def test_step05():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_step06():
    c = Circle(4)
    d = eval(repr(c))
    assert d == c


def test_step07():
    c1 = Circle(2)
    c2 = Circle(4)
    c_add = c1 + c2
    assert c_add == Circle(6)

    c_mult = c2 * 3
    assert c_mult == Circle(12)


def test_step08():
    c1 = Circle(2)
    c2 = Circle(4)
    more = c1 > c2
    assert more == False

    less = c1 < c2
    assert less == True

    equal = c1 == c2
    assert equal == False

    c3 = Circle(4)
    assert c2 == c3


def test_sort():
    circles = [Circle(3), Circle(0), Circle(2)]
    circles.sort()
    circles_sort = [Circle(0), Circle(2), Circle(3)]
    assert circles == circles_sort


