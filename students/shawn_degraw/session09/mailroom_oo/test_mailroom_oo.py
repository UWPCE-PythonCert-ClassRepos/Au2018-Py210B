#!/usr/bin/env python

"""Pytest unit tests for the mailroom_oo module."""

from mailroom_oo.donor_models import *


def test_donor_init():
    d1 = Donor("Shawn DeGraw")
    d2 = Donor("Brandon Nguyen", 5000)

    assert d1.name == "Shawn DeGraw"
    assert d1.donations == []

    assert d2.name == "Brandon Nguyen"
    assert d2.donations == [5000]


def test_donor_manipulation():
    d1 = Donor("Shawn DeGraw")

    d1.add_donation("Shawn DeGraw", 5000)
    d1.add_donation("Shawn DeGraw", 2000)
    d1.add_donation("Shawn DeGraw", 3000)

    assert d1.donations == [5000, 2000, 3000]
    assert d1.number_donations == 3
    assert round(d1.average_donation, 2) == 3333.33
