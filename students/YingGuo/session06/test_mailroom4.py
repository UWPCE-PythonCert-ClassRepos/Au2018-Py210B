#!/usr/bin/env python

"""session06, write test code for mailroom"""

from mailroom4 import report
from mailroom4 import all_letter
from mailroom4 import donor_list
from mailroom4 import letter_print
from mailroom4 import add_new_donor
from mailroom4 import letter_all
from mailroom4 import all_letter
import os

#test donor list 
def test_donor_list():
    data = {"Tom":[100,200], "Tim":[3000]}
    expected = ["Tom", "Tim"]
    actual = donor_list(data)
    assert expected == actual

#test letter print
def test_letter_print():
    name = "Ying"
    amount = 8888
    expected = "Thank you Ying for your donation 8888!"
    actual = letter_print(name, amount)
    assert expected == actual

#test new donor func
def test_add_update_new_donor():
    data = {"Tom":[100,200]}
    name = "Ying"
    amount = 8888
    expected = {"Tom":[100,200], "Ying":[8888]}
    actual = add_new_donor(data, name, amount)
    assert expected == actual

#test report func
def test_report():
    data = {"Tom":[100,200], "Tim":[3000]}
    expected = [("Tim", 3000, 1, 3000), ("Tom", 300, 2, 150)]
    actual = report(data)
    assert expected == actual

#test letter_all which send thank you letter to existing donors
def test_letter_all():
    name = "Ying"
    total_donation = 8888
    expected = "Dear Ying, Thank you for your total donation of 8888"
    actual = letter_all(name, total_donation)
    assert expected == actual

#test all_letter which creats file
def test_created_file():
    data = {"Tom":[100,200]}
    all_letter(data)
    assert os.path.isfile("Tom")
