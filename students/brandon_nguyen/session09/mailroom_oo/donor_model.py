#!/usr/bin/env python3
# Week9 Excercise donor_models.py
# Student: Brandon Nguyen - Au2018

from datetime import datetime, date


# contant to use in all classes
E_FORMAT = "\n".join(("", "Dear {Name},", "", "Thank you for your "
                          "recent donation of {LastAmnt:.2f}.",
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
        return rpt_row.format(self.name, self.total_donation,
                              self.number_donations, "$",
                              self.average_donation)

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

    # DONOT expose!
    # @property
    # def donor_db(self):
    #     return self.__donor_db

    # method to update donation
    def add_donor_db(self, name, donation=None):
        """ To add donor and donation into collection"""
        if name not in self.__donor_db:
            self.__donor_db[name] = Donor(name)
        self.__donor_db[name].add_donation(donation)

    def list_donors(self):
        """ quick way to return a list of names in db """
        # lst_names = []
        # [lst_names.append(name) for name in self.__donor_db.keys()]
        # Way cleaner way from above to this:
        lst_names = list(self.__donor_db.keys())
        return sorted(lst_names)

    def get_donor_data(self, name):
        """need this to assign back to sigle donor use in thank you"""
        return self.__donor_db[name]

    def list_rpt_data(self, donorName=None):
        """ Return a sorted list of report rows for all donors """
        header_txt = ("Donor Name              |  Total Given  | Num Gifts |"
                      " Average Gift")
        lst_rpt = [header_txt]
        lst_donors = self.list_donors()
        # if method call does not have donorName parameter return all
        if not donorName:
            [lst_rpt.append(self.get_donor_data(person).donor_rpt_row())
                for person in self.list_donors()]  # harder to read this!
        elif donorName in lst_donors:
            lst_rpt.append(self.get_donor_data(donorName).donor_rpt_row())
        # TODO more: Think of catcing error or no name exist?.
        return "\n".join(lst_rpt)

    def ty_letter_all(self):
        """This is to return a list of stuples of donor's latter and filename"""
        letters_list = []
        for personName in self.list_donors():
            letter = self.get_donor_data(personName).ty_letter()
            textfile = (personName.replace(" ", "_") + "_" +
                        str(date.today()).replace(" ", "_")+".txt")
            letters_list.append((letter, textfile),)
        return letters_list

# TODO:
    # 4) more errors handling?
