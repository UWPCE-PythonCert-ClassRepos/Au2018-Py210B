#!/usr/bin/env python3

"""
Class: Python 210 B, Au2018
Exercise: Session 09, Object Oriented Mailroom
Student: Jason Jakubiak

Object oriented approch to the mailroom exercise
"""

class Donor:

    def __init__(self, name, donation=None):
        self.__name = name
        self.__donation = []
        if donation is not None:
            self.__donation.append(donation)


    @property
    def name(self):
        return self.__name

    @property
    def donation(self):
        return self.__donation

    @property
    def total_donation(self):
        return sum(self.__donation)

    @property
    def cnt_donation(self):
        return len(self.__donation)

    @property
    def avg_donation(self):
        return self.total_donation / self.cnt_donation

    def add_donation(self, amt):
        self.__donation.append(amt)



class DonorCollection:
    def __init__(self):
        self.__donor_db = {}

    def add_donor(self, name):
        if name in self.__donor_db:
            raise ValueError(' Name ({}) already exists'.format(name))
        self.__donor_db[name] = Donor(name)
        return name

    def add_donation(self, name, donation):
        self.__donor_db[name].add_donation(donation)


    @property
    def donors(self):
        return self.__donor_db.values()

    def donor_list(self):
        donor_list = []
        for donor in self.donors:
            donor_list.append(donor)
        return "\n".join(donor_list)

test_db = {
    "jeff": [183.00, 200.00],
    "alex": [53898.23, 2653.00, 105.07],
    "paul": [33941.98],
    "mark": [1.65, 55.00],
    "john": [2705.71],
    }


donor_list

# class DonorCollection:

#     def __init__(self):
#         self.__donors = {}
    
#     def add_new_donor(self, name):
#         if name in self.__donors:
#             raise ValueError(' Name ({}) already exists'.format(name))
#         self.__donors[name] = Donor(name)

#     def add_donation(self, name, donation):
#         self.__donors[name].add_donation(donation)

#     def generate_report_row(self):
#         return '{}{}{}{}'.format(self.__name, self.num_donations
#                                 , self.total_donations, self.avg_donation
#                                 )

#     def get_donor(self, name):
#         return self.__donors[name]

#     def generate_report(self):
#         header = '|{}|{}|{}|{}|'.format('Name', 'Donations', 'Total', 'Average')
#         lines = [header]
#         for donor in self.__donors.values():
#             lines.append(self.generate_report_row())
#         return '\n'.join(lines)




test_db = {
    "jeff": [183.00, 200.00],
    "alex": [53898.23, 2653.00, 105.07],
    "paul": [33941.98],
    "mark": [1.65, 55.00],
    "john": [2705.71],
    }

dc = DonorCollection()
dc.donor_list



## TEST DONOR()
d = ()
d = Donor('Bill Gates', 1000)
d.donation
d.total_donation
d.cnt_donation
d.avg_donation
d.add_donation(2000)

## TEST DONOR)_COLLECTION()
dc = DonorCollection()
dc.add_donor('Bill Gates')
dc.add_donation('Bill Gates', 1234)
d = dc.get_donor('Bill Gates')
d.total_donation
d.cnt_donation
d.avg_donation
d.add_donation(500)
d.name
d.total_donation
d.cnt_donation
d.avg_donation

    # NOT WORKING
    dc.generate_report
    d.total_donation
    test_db = Donor


## TEST DONOR()
# def test_donor():
#     d = Donor('Bill Gates', 1000)
#     assert d.donation = [1000]
#     assert d.total_donation == 1000
#     assert d.cnt_donation == 1
#     assert d.avg_donation == 1000
#     d.add_donation(2000)
#     assert d.donation = [1000, 2000]
#     assert d.total_donation == 3000
#     assert d.cnt_donation == 2
#     assert d.avg_donation == 1500


