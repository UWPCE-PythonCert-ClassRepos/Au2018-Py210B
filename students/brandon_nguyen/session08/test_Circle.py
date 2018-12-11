# Week8 Excercise test circle -
# Student: Brandon Nguyen - Au2018

import pytest
from math import pi
from Circle import *


######################
# step 1 test: radius in circle
#####################
def test_circle_radius():
    c = Circle(4)
    assert c.radius == 4


def test_circle_radius0():
    """ test value error trap """
    with pytest.raises(ValueError):
        # c = Circle(2)  # failed test- Failed: DID NOT RAISE
        c = Circle(-1)
        c = Circle(0)

# use this example to ask about 
# Failed: DID NOT RAISE <class 'AttributeError'>
# Test for expected failure!

# def test_circle_read_only_r():
#     with pytest.raises(AttributeError) as err:
#         c = Circle(1)
#         c.radius = 5  #without setter code this code pass


##################################
# step 2 and 3 test: diameter and new r in circle
###################################
def test_circle_diameter():
    c = Circle(2)
    assert c.diameter == 4

    # set a new diameter value expecting new r
    c.diameter = 8
    assert c.radius == 4
    # set a new radius value expecting new diameter
    c.radius = 5
    assert c.diameter == 10


##################################
# step 4 test: area property
###################################
def test_circle_area():
    c = Circle(2)
    assert round(c.area, 2) == round(pi*(c.radius**2), 2)


##################################
# step 5 test: class method from_diameter
###################################
def test_circle_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


##################################
# step 6 test: __str__, __repr__
###################################
def test_circle_repr():
    c = 'Circle(4)'
    d = eval(repr(c))
    assert d == c


##################################
# step 7 test: add and multiply 2 circles
###################################
def test_circle_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c2 + c1).radius == 6


def test_circle_multiply():
    c2 = Circle(4)
    assert (c2*3).radius == 12
    assert isinstance((c2*3), Circle)
