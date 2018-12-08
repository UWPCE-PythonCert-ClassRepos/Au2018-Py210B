#!/usr/bin/env python

""" Mailroom_oo - refactor in oject oriented design """


class Donor:
    """ Donor object
    :param name: donor's name
    :param initial_donation: optional initial donation value
    """

    def __init__(self, name, initial_donation=None):
        self.__name = name
        self.__donations = []
        if initial_donation is not None:
            self.__donations.append(initial_donation)
            self.average_donation = initial_donation

    @property
    def name(self):
        return self.__name

    @property
    def donations(self):
        return self.__donations

    @property
    def totaldonations(self):
        return sum(self.__donations)

    @property
    def number_donations(self):
        return len(self.__donations)

    def __str__(self):
        return "{}, {}".format(self.__name, self.__donations)

    def add_donation(self, name, donation):
        """
        adds a new donation to the list
        and recalculates the average donation
        """

        self.__donations.append(donation)
        self.average_donation = sum(self.donations) / self.number_donations


class DonorCollection:
    """
    Holds collection of donor objects
    and code to operate on entire collection
    """

    # Thank you letter templates
    THANK_YOU_LETTER = "\n".join(("", "Dear {name},", "", "Thank you for your "
                                  "generous donation of ${amount:.2f} to our "
                                  "cause.", "Your donations help keep Python "
                                  "great!", "", "Sincerely", "", "The Python "
                                  "Project", ""))

    GENERAL_DONATION_LETTER = "\n".join(("", "Dear {name},", "", "Thank you for "
                                         "your generosity in supporting us with "
                                         "${totaldonation:.2f} in donations.",
                                         "We hope to have your continued support.",
                                         "", "With great thanks", "", "The Python "
                                         "Project"))

    def __init__(self):
        self.donor_collection = []

    def donor_update(self, name, initial_donation=None):
        """ Method to add donation if donor exists or
        creates new Donor object if the donor does not exist
        """

        donor = self.search_name(name)
        if donor:
            donor.add_donation(name, initial_donation)
        else:
            self.donor_collection.append(Donor(name, initial_donation))

    def report_header(self):
        return "{:<26}|{:^13}|{:^11}|{:^14}".format("Donor Name", "Total Given",
                                                    "Num Gifts", "Average Gift")

    def create_report(self):
        reportbody = self.report_header()
        for donor in self.collect_data():
            dobject = self.search_name(donor)
            reportbody = "\n".join([reportbody, "{:<27}${:>11.2f} {:>11d}  ${:>12.2f}".format(dobject.name,
                                    dobject.totaldonations / 100, dobject.number_donations, dobject.average_donation / 100)])
        return reportbody

    def search_name(self, searchname):
        """ Searches collection and returns Donor object if exists """

        for donor in self.donor_collection:
            if donor.name == searchname:
                return donor
        return None

    def donor_namelist(self):
        """ Creates and returns a list of donor names from collection """

        donorlist = []
        for donor in self.donor_collection:
            donorlist.append(donor.name)
        return donorlist

    def collect_data(self):
        """ Creates sorted list of donors """

        letterdata = {}
        for donor in self.donor_collection:
            letterdata[donor.name] = donor.totaldonations / 100

        return sorted(letterdata)
