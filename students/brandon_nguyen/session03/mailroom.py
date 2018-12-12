#!/usr/bin/env python3
# Week3 Excercise mailroom part 1 with correction
# Student: Brandon Nguyen - Au2018

import sys
import unittest
from decimal import Decimal

# global define data structure
donor_db = [("Brandon Nguyen", [4500.33, 350.87, 300.05]),
            ("Shawn DeGraw", [5500.00, 345.05, 571.33]),
            ("Jacqueline Lee", [4300.00, 3200.00, 230.13]),
            ("Aidan Nguyen", [4300.00, 200.00, 238.23]), ]

promptTxt = "\n".join(("Welcome to the mailroom program!",
                       "Please choose from below 3 options:",
                       "1 - Send a Thank You",
                       "2 - Create a Report",
                       "3 - Quit",
                       ">>> "))


# think about a main menu function that can be called any where.
def main_menu():
    promptTxt = "\n".join(("Welcome to the mailroom program!",
                           "Please choose from below 3 options:",
                           "1 - Send a Thank You",
                           "2 - Create a Report",
                           "3 - Quit",
                           ">>> "))


def send_ty():
    while True:
        response = input("\nPlease enter donor full names or \"list\"."
                         " Q to return to main menu: ")
        if response.strip() == 'list':
            list_donors()
        elif response.strip() == 'Q':
            main()
        else:
            donation = input("Please enter donation amount for " + response +":>>")
            # New name add donation
            if response not in donor_db:
                donor_db.append((response.strip(), [float(donation)]))
            # existing name add donation
            else:
                name[0] == response.strip()
                indx = donor_db.index(name)
                donor_db[indx][1].append(float(donation))
            print("\n\nHello {},\nThank you so much for the generious"
                  "donation of {}!\n\n".format(response.strip(),
                                               float(donation)))


def create_rpt():
    """
    This function is to print the report of donor.  
    """
    # Currently need more work on the format as 0.0 problem not yet solved.
    print()
    # creating a new list with sorted total in reverse already for printing.
    newList = sort_sum()
    header_string = "Donor Name              |  Total Given | Num Gifts | Average Gift"
    line = '-'*len(header_string)
    print(header_string)
    print(line)
    for donor, total, num, avg in newList:
     # correction here
        print(" {:<18}     $  {:>12.2f} {:>6} {:>6} {:>8.2f}".
              format(donor, total[0], num[0], "$", avg[0]))
    print("\n\n")


def sort_sum():
    # creating a new list with computed value for easy printing.
    """
    This function returned a sorted list of by on order amount3
    """
    dbSum = []
    for name, donation in donor_db:
        dbSum.append((name, [round(sum(donation), 2)], [len(donation)],
                            [round(sum(donation)/len(donation), 2)]),)
    return sorted(dbSum, key=lambda donor: donor[1], reverse=True)


def list_donors():
    """
    Basic Name of donor return in Order by First Name
    """
    lst = []
    for name in donor_db:
        lst.append(name[0])
    lst.sort()
    print()
    for name in lst:
        print(name)
    print()


def quit_program():
    print("Thank you for trying mailroom!")
    sys.exit()  # reason to import sys


def main():
    while True:
        response = input(promptTxt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection   
        if response == "1":
            send_ty()
        elif response == "2":
            create_rpt()
        elif response == "3":
            quit_program()
        else:
            print("\nNot a valid option! Please enter value 1,2 or 3.\n")


if __name__ == '__main__':
    # ask the intend of the comment in class
    main()
