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

    # test last donation call
    d1.add_donation(255)
    d1.add_donation(256)
    assert d1.donations[-1] == 256
    print(d1.donations[-1])

    print(d1.donations)

    Test_letter = "\n".join(("", "Dear Aidan Nguyen,", "",
                            "Thank you for your "
                             "kind donation of 256.00.",
                             "It will be put to very good use.", "",
                             "Sincerely, ", "", "-The Team\n"))
    assert Test_letter == d1.ty_letter()
    print(d1.ty_letter())
    # test a single report row for 1 donor
    test_report_txt =" Name Test              $        300.00      2      $   310.00"
    d2_rpt_row = d2.donor_rpt_row()
    assert d2_rpt_row == test_report_txt

    print(d2_rpt_row)

    #assert False


###############################################
# Test DonorCollection: class method/properties
###############################################
def test_donor_Collection_all():

    # test store donors to collection we had 3 donors up to this point
    db = DonorCollection()

    # Test add basic
    db.add_donor_db("Brandon Nguyen", 500)
    db.add_donor_db("Shawn Degraw", 200)

    lst = db.list_donors()
    for name in db.donor_db.keys():
        print(name)

    print(db.list_donors())

    for name in db.list_donors():
        print(name)
    
    # test get_name to see if we can extract donor this way
    donorBN = db.get_name("Brandon Nguyen")
    assert donorBN.donations[-1] == 500
    
    #assert False

# TODO:
    # 1) breakdown the test
    # 2) test the rest of the methods and attribute/properties