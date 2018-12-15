#!/usr/bin/env python

import os
import unittest
import mailroom4 as mailroom



"""
unit tests for the mailroom program
"""

def test_user_Report():
    """ test the user report """

    donor_db = {"William Gates": [653772, 12.17]}
    report = mailroom.user_Report(donor_db)
    print(report)
    assert report.startswith("William Gates")
    assert report.endswith("326892")


def test_send_letters():
    """
    This only tests that the files get created, but that's a start

    Note that the contents of the letter was already
    tested with test_gen_letter
    """

    mailroom.send_letters()

    assert os.path.isfile('Jeff Bezos.txt')
    assert os.path.isfile('William Gates.txt')
    # check that it'snot empty:
    with open('William Gates.txt') as f:
        size = len(f.read())
    assert size > 0


def test_generate_txt():

    donor_name = "William Gates"
    test_txt = mailroom.generate_txt(donor_name)
    print(test_txt)
    assert test_txt == ('''Hello William Gates,
        Thank you for your donation to the organization, this is a thank you email to show our appreciation.
        ''')



if __name__ == "__main__":
 
    # test_generate_txt()
    test_send_letters()
    test_user_Report()
    print("All tests Passed")
