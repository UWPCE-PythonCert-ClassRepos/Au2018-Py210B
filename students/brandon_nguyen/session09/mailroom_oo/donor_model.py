#!/usr/bin/env python3
# Week9 Excercise donor_models.py
# Student: Brandon Nguyen - Au2018


# contant to use in all classes
E_FORMAT = "\n".join(("", "Dear {Name},", "", "Thank you for your "
                          "kind donation of {LastAmnt:.2f}.",
                          "It will be put to very good use.", "",
                          "Sincerely, ", "", "-The Team\n"))


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

    def ty_letter(self):
        # return the print out letter base on the last donation
        return E_FORMAT.format(Name=self.__name, LastAmnt=self.__donations[-1])

    def donor_rpt_row(self):
        rpt_row = " {:<18}     $  {:>12.2f} {:>6} {:>6} {:>8.2f}"
        return rpt_row.format(self.__name, self.__total_donation,
                              self.__number_donations, "$",
                              self.__average_donation)

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
    """ This class will hold:
            -all Donor objects
            -methods to add new donor, search for a given donor
            - extract donor
            -create report
            -send thank you letters to all
    """
    def __init__(self):
        self.__donor_db = {}
    # We need data structure and other constants for printing

    @property
    def donor_db(self):
        return self.__donor_db

    # method to update donation
    def add_donor_db(self, name, donation=None):
        """ To add donor into collection"""
        # How best to handle existing donor?
        # TODO existing donor only take donation?

        # assume donation is ok TODO more
        self.__donor_db[name] = Donor(name)
        self.__donor_db[name].add_donation(donation)

    def list_donors(self):
        """ quick way to return a list of names in db """
        lst_names = []
        [lst_names.append(name) for name in self.__donor_db.keys()]
        lst_names.sort()
        return lst_names

    # method to return donor in db or collection getName?
    def get_name(self, name):
        """need this to assign back to sigle donor"""
        return self.__donor_db[name]

# TODO:
    # 1) method create report maybe also search?
    # 2) method to send thank you to all
    # 3) update donation on existing donor
    # 4) more errors handling


