#!/usr/bin/env python

'''
donor_models.py:  Holds classes for Object-Oriented Mailroom assignment.
Written by David K. Arasim ~ December 6, 2018
'''

'''Global varibles for list of Donors and report with donation summary:
Donor Name|Total Given|Num Gifts|Average Gift'''
donor_name = 'Donor Name'
donor_list = 'List of Donors'
tot_given = 'Total Given'
num_gifts = 'Num Gifts'
avg_gift = 'Average Gift'
sep_char = '|'

donor_name_w = 26
donor_list_w = 26
tot_given_w = 13
num_gifts_w = 11
avg_gift_w = 13
sep_char_w = len(sep_char)


class Donor(object):
    def __init__(self, name, initial_donation=None):
        self._name = name
        self._donations = []

        if initial_donation is not None:
            self._donations.append(float(initial_donation))

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def total_donation(self):
        return sum(self.donations)

    @property
    def avg_donation(self):
        if self.num_donations == 0:
            return 0
        else:
            return self.total_donation / self.num_donations    

    def __str__(self):
        # Re-defines what str() function will produce
        amts_str = ','.join(str(x) for x in self.donations)
        return "{}:{}".format(self.name, amts_str)

    def add_donation(self, donation):
        self._donations.append(float(donation))

    def generate_report_row(self):
        # Generate single report row
        row_format = self.name, donor_name_w, self.total_donation, (tot_given_w - 1)
        row_format += self.num_donations, num_gifts_w, self.avg_donation, (avg_gift_w - 1)
        return '{:{}} ${:{}.2f} {:{}} ${:{}.2f}'.format(*row_format)

    def generate_list_row(self):
        # Generate single list row
        row_format = self.name, donor_list_w
        return '{:{}}'.format(*row_format)


class DonorCollection(object):
    def __init__(self, donor_file=None):
        self.donors = {}  # Donor Name/Donation pairs

        if donor_file is None:
            self.donor_file = None
        else:
            self.donor_file = donor_file
            self.build_donor_dict()

    def build_donor_dict(self):
        '''Build Donor Dictionary by importing data from a text file'''
        try:
            with open(self.donor_file, 'r') as donorfile:
                while True:
                    donor_line = donorfile.readline()
                    if not donor_line: break

                    donor_name, donor_amts = donor_line.strip().split(':')

                    self.add_new_donor(donor_name)
                    
                    for amt in donor_amts.split(','):
                        self.add_donation(donor_name, amt)

            donorfile.close()
        except FileNotFoundError:
            # Handle the error here as needed (not implemented)
            pass

    def build_donor_text(self):
        '''Export the Donor Dictionary data to a text file'''
        if self.donor_file is not None:
            with open(self.donor_file, 'w') as donorfile:
                for donor in self.donors:
                    this_line = str(self.get_donor(donor)) + '\n'
                    donorfile.write(this_line)

            donorfile.close()

    def add_new_donor(self, name):
        if name not in self.donors:
            # Prevents clobbering existing Donor record
            self.donors[name] = Donor(name)

    def add_donation(self, name, donation):
        if name not in self.donors:
            # Auto-install new donor if they aren't already in there 
            self.donors[name] = Donor(name)

        self.donors[name].add_donation(donation)    

    def get_donor(self, name):
        if name in self.donors:
            return self.donors[name]
        else:
            return 'Name not found'

    def generate_report(self):
        # Report header nomenclature
        header_nom = donor_name, donor_name_w, sep_char
        header_nom += tot_given, tot_given_w, sep_char
        header_nom += num_gifts, num_gifts_w, sep_char
        header_nom += avg_gift, avg_gift_w
        rpt_lines = ['{:{}}{}{:>{}}{}{:>{}}{}{:>{}}'.format(*header_nom)]

        # Report header/rows separator
        header_sep = '-'*donor_name_w + '-'*sep_char_w 
        header_sep += '-'*tot_given_w + '-'*sep_char_w
        header_sep += '-'*num_gifts_w + '-'*sep_char_w 
        header_sep += '-'*avg_gift_w
        rpt_lines.append(header_sep)

        # Report rows
        for donor in self.donors.values():
            rpt_lines.append(donor.generate_report_row())

        return '\n'.join(rpt_lines)

    def generate_list(self):
        # List header nomenclature
        header_nom = donor_list, donor_list_w
        list_lines = ['{:{}}'.format(*header_nom)]

        # List header/rows separator
        header_sep = '-'*donor_list_w
        list_lines.append(header_sep)

        # Report rows
        for donor in self.donors.values():
            list_lines.append(donor.generate_list_row())

        return '\n'.join(list_lines)

    def build_thank_you_list(self):
        thank_you_list = []

        for donor in self.donors:
            thank_you_list.append(str(self.get_donor(donor)))

        return thank_you_list
