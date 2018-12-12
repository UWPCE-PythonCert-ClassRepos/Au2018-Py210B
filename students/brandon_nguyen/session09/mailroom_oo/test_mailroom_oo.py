# Week9 Excercise test_mailroom_oo.py
# Student: Brandon Nguyen - Au2018

import pytest
from mailroom_oo.donor_model import *


#  Let try to write all test first including what already in class.
##############################################
# Test Donor class and its method/properties
##############################################

def test_donor_basic():
    d0 = Donor("Andrew Nguyen")
    d1 = Donor("Aidan Nguyen", 200)
    d2 = Donor("Name Test", 300)

    # these 3 test was working with None assign to initial
    assert d0.name == "Andrew Nguyen"
    assert d0.number_donations == 0
    assert d0.average_donation == 0  # solved devision by 0

    assert d1.average_donation == 200
    assert d1.total_donation == 200
    assert d2.total_donation == 300

    # Some donor.add(value) calls then retest
    d0.add_donation(200)
    d1.add_donation(300)
    d2.add_donation(320)

    assert d1.donations == [200, 300]

    assert d0.number_donations == 1
    assert d1.average_donation == 250
    assert d2.average_donation == 310
    assert d2.number_donations == 2
    assert d2.total_donation == 620

###############################################
# Test DonorCollection: class method/properties
###############################################
