
"""
Class: Python 210 B, Au2018
Exercise: Session 09, Test Object Oriented Mailroom
Student: Jason Jakubiak

Test code for the object oriented mailroom exercise
"""

from donor_models import *
import pytest

def test_donor_class():
    d = Donor('Bill Gates', 1000)
    assert d.name == 'Bill Gates'
    assert d.donation == [1000]
    assert d.total_donation == 1000
    assert d.cnt_donation == 1
    d.add_donation(10000)
    assert d.avg_donation == 1000