#!/usr/bin/env python

"""Pytest unit tests for the mailroom_oo module."""

from mailroom_oo.donor_models import *


def test_donor_init():

    # Testing for initialization name and donation in cents
    d1 = Donor("Shawn DeGraw", 1000)
    d2 = Donor("Brandon Nguyen", 5000)

    assert d1.name == "Shawn DeGraw"
    assert d1.donations == [1000]

    assert d2.name == "Brandon Nguyen"
    assert d2.donations == [5000]


def test_donor_manipulation():

    d1 = Donor("Shawn DeGraw", 2000)

    d1.add_donation("Shawn DeGraw", 5000)
    d1.add_donation("Shawn DeGraw", 8000)

    assert d1.donations == [2000, 5000, 8000]
    assert d1.number_donations == 3
    assert round(d1.average_donation, 2) == 5000.0


def test_invalid_donationentry():

    dc1 = DonorCollection()

    assert not dc1.donor_update("test")
    assert not dc1.donor_update("test", "stringvalue")


def test_invalid_nameentry():

    dc2 = DonorCollection()
    dc2.donor_update("  Test   User  ", 20)

    assert dc2.search_name("Test User")
    assert dc2.search_name("  Test    User  ")


def test_donorcollection():

    dc2 = DonorCollection()

    dc2.donor_update("Jane Doe", 20.00)
    dc2.donor_update(" jane  doe ", 30.00)

    assert dc2.search_name("Jane Doe").name == "Jane Doe"
    assert dc2.search_name("Jane Doe").donations == [2000, 3000]
    assert dc2.search_name("jane doe").name == "Jane Doe"

    assert dc2.collect_data() == ['Jane Doe']


def test_report():

    dc2 = DonorCollection()
    dc2.donor_update("Jane Doe", 20.00)

    assert dc2.create_report() == '\nDonor Name                | Total Given | Num Gifts | Average Gift \n------------------------------------------------------------------\nJane Doe                   $      20.00           1  $       20.00'

    assert dc2.report_header() == '\nDonor Name                | Total Given | Num Gifts | Average Gift \n------------------------------------------------------------------'


def test_donorcollection_sort():

    dc1 = DonorCollection()

    dc1.donor_update("Zoe", 100.00)
    dc1.donor_update("Sent", 150.00)
    dc1.donor_update("Sent", 200.00)
    dc1.donor_update("Beta", 200.00)
    dc1.donor_update("Alpha", 10.00)
    dc1.donor_update("Gamma", 80.00)

    assert dc1.collect_data() == ['Alpha', 'Beta', 'Gamma', 'Sent', 'Zoe']
    assert dc1.search_name(dc1.collect_data()[0]).donations == [1000]
    assert dc1.search_name(dc1.collect_data()[3]).donations == [15000, 20000]
