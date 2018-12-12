#!/usr/bin/env python3
# Week9 Excercise donor_models.py
# Student: Brandon Nguyen - Au2018


class Donor:
    """ Donor object - concept from mailroom1
    :param name: donor's name
    :param initial_donation: optional initial donation value
    """

    def __init__(self, name, initial_donation=None):
        self.__name = name
        self.__donations = []
        if initial_donation is not None:
            self.__donations = [initial_donation]
            self.__average_donation = initial_donation
            self.__total_donation = initial_donation
            self.__number_donations = 1

    def add_donation(self, donation):
        self.__donations.append(donation)

    @property
    def name(self):
        return self.__name

    @property
    def donations(self):
        return self.__donations

    @property
    def number_donations(self):
        self.__number_donations = len(self.__donations)
        return self.__number_donations

    @property
    def total_donation(self):
        return sum(self.__donations)

    @property
    def average_donation(self):
        try:
            self.__average_donation = self.total_donation/self.number_donations
        except ZeroDivisionError:
            self.__average_donation = 0
        return self.__average_donation

    def __str__(self):
        return f"{self.__name}, {self.__donation}"


class DonorCollection:
    # Revew mailroom 1 instruction to do the following
    # We need data structure and other constants for printing

    # method to update donation

    # method to return donor in list getName?

    # method create report

    # method to send thank you.

    pass