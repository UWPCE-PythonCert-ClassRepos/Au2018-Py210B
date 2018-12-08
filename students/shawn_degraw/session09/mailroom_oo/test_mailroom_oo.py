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


def test_donorcollection():

    dc1 = DonorCollection()
    dc2 = DonorCollection()

    dc1.donor_update("John Doe")
    dc2.donor_update("Jane Doe", 2000)

    assert dc1.search_name("John Doe").name == "John Doe"
    assert dc1.search_name("John Doe").donations == []
    assert dc2.search_name("Jane Doe").name == "Jane Doe"
    assert dc2.search_name("Jane Doe").donations == [2000]

    assert dc2.donor_namelist() == ['Jane Doe']
    assert dc2.collect_data() == ['Jane Doe']

    assert dc2.create_report() == 'Donor Name                | Total Given | Num Gifts | Average Gift \nJane Doe                   $      20.00           1  $       20.00'

    assert dc2.report_header() == 'Donor Name                | Total Given | Num Gifts | Average Gift '


def test_donorcollection_multi():

    dc1 = DonorCollection()

    dc1.donor_update("Zoe", 100)
    dc1.donor_update("Sent", 150)
    dc1.donor_update("Beta", 200)
    dc1.donor_update("Alpha", 10)
    dc1.donor_update("Gamma", 80)

    assert dc1.collect_data() == ['Alpha', 'Beta', 'Gamma', 'Sent', 'Zoe']
