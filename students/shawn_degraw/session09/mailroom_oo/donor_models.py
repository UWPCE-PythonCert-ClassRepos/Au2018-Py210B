#!/usr/bin/env python

""" Mailroom_oo - refactor in oject oriented design """


class Donor:
    """ Donor object containing all donor specific data
    :param name: donor's name
    :param initial_donation: initial donation value in cents
    """

    def __init__(self, name, initial_donation):
        self.__name = name
        self.__donations = [initial_donation]
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
        Adds a new donation to the donor's list
        and recalculates the average donation
        """

        self.__donations.append(donation)
        self.average_donation = sum(self.donations) / self.number_donations


class DonorCollection:
    """
    Holds collection of donor objects in a list
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
        """
        Method to add donation if donor exists or
        creates new Donor object if the donor does not exist.
        Returns True if actions are successful.
        Controls donation data and name data.
        """

        # Validate the content of initial_donation and format it for storage
        if not initial_donation:
            return False
        else:
            try:
                formatted_donation = int(float(initial_donation) * 100)
            except ValueError:
                return False

        if formatted_donation < 1:
            return False

        # Storing name without extra spaces
        formatted_name = " ".join(name.split())

        # Create donor or update existing donor
        donor = self.search_name(formatted_name)
        if donor:
            donor.add_donation(formatted_name, formatted_donation)
            return True
        else:
            self.donor_collection.append(Donor(formatted_name, formatted_donation))
            return True

    def report_header(self):
        """ Creates and returns report header as a string. """

        return "\n{:<26}|{:^13}|{:^11}|{:^14}\n{}".format("Donor Name", "Total Given",
                                                    "Num Gifts", "Average Gift", "-" * 66)

    def create_report(self):
        """ Generates report line by line and returns report as a string """

        reportbody = self.report_header()
        for donor in self.collect_data():
            dobject = self.search_name(donor)
            reportbody = "\n".join([reportbody, "{:<27}${:>11.2f} {:>11d}  ${:>12.2f}".format(dobject.name,
                                    dobject.totaldonations / 100, dobject.number_donations, dobject.average_donation / 100)])
        return reportbody

    def search_name(self, searchname):
        """
        Searches collection by donor name
        and returns Donor object if exists """

        for donor in self.donor_collection:
            if donor.name.lower() == " ".join(searchname.split()).lower():
                return donor
        return None

    def collect_data(self):
        """ Creates and returns sorted list of donor names """

        letterdata = {}
        for donor in self.donor_collection:
            letterdata[donor.name] = donor.totaldonations / 100

        return sorted(letterdata)

    def write_letters(self):
        """ Write a letter to a file for each donor. """

        for name in self.collect_data():
            filename = name.replace(' ', '_') + ".txt"

            formatdict = {"name": name, "totaldonation": self.search_name(name).totaldonations / 100}
            try:
                with open(filename, 'w') as outfile:
                    outfile.write(self.GENERAL_DONATION_LETTER.format(**formatdict))
            except IOError:
                return False
        return True
