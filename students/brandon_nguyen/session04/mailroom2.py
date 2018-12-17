#!/usr/bin/env python3
# Week3 Excercise mailroom part 2
# Student: Brandon Nguyen - Au2018

import sys
import unittest
from decimal import Decimal
from datetime import datetime, date

# global define data structure
# dictionary {person:[donations]}
donor_db = {"Brandon Nguyen": [4500.33, 350.87, 300.05],
            "Shawn DeGraw": [5500.00, 345.05, 571.33],
            "Jacqueline Lee": [4300.00, 3200.00, 230.13],
            "Aidan Nguyen": [4300.00, 200.00, 238.23],
            }
promptText = "\n".join(("\nWelcome to the mailroom program!\n",
                        "Please choose an options:\n\n",
                        "1 - Send a Thank You to a single donor.",
                        "2 - Create a Report.",
                        "3 - Send letters to all donors.",
                        "q - Quit",
                        ">>> "))

subMenuPrompt = ("Please Chose an option:\n\nlist - To display a list of "
                 "current donors.\n"
                 "1    - To enter name of donor to update.\n"
                 "q    - To exit this menu.\n"
                 ">>> ")
# building switch case menu with dictionary


# think about a main menu function that can be called any where.
def show_menu(promptxt, select_dict):
    while True:
        menu_selected = input(promptxt)
        if select_dict[menu_selected]() == "Exit Menu":
            break


def send_ty():
    show_menu(subMenuPrompt, sub_menu_dict)


def create_rpt():
    """
    This function is to print the report of donor.  
    """
    # Currently need more work on the format as 0.0 problem not yet solved.
    print()
    newList = sort_sum()  # creating a new list with sorted total in reverse.
    header_string = "Donor Name              |  Total Given | Num Gifts | Average Gift"
    line = '-'*len(header_string)
    print(header_string)
    print(line)
    rept_txt_fmt = " {:<18}     $  {:>12.2f} {:>6} {:>6} {:>8.2f}"
    for donor, total, num, avg in newList:
        print(rept_txt_fmt.format(donor, total[0], num[0], "$", avg[0]))
    print("\n\n")


def sort_sum():
    # creating a new list with computed value for easy printing.
    """
    This function returned a sorted list of by on order amount3
    """
    dblist = []
    dbSum = []
    # quick way to convert back to list to reuse existing code.
    for i, j in donor_db.items():
        dblist.append((i, j))
    for name, donation in dblist:
        dbSum.append((name, [round(sum(donation), 2)], [len(donation)],
                            [round(sum(donation)/len(donation), 2)]),)
    return sorted(dbSum, key=lambda donor: donor[1], reverse=True)


def list_donors():
    """
    Basic Name of donor return in Order by First Name
    """
    lst = []
    print()
    for person in donor_db:
        lst.append(person)
    lst.sort()
    for name in lst: 
        print(name)
    print()


def update_donation():
        input_person = input("\nPlease enter donor full names: ")
        input_donation = float(input("Please enter donation amount for " +
                                     input_person + ":>> "))
        # existing people add to donation
        if input_person in donor_db:
            new_Donation = donor_db.get(input_person)
            new_Donation.append(input_donation)
            donor_db[input_person] = new_Donation
        else:
            donor_db.update({input_person: [input_donation]})
        print()
        print(email_template(input_person, input_donation))


def email_template(name, newAmout):
    e_frmt = {
                  0: 'Dear',
                  1: 'Thank you for your kind donation of ',
                  2: 'It will be put to very good use',
                  3: 'Sincerely, ',
                  4: '-The Team'
                  }
    # Not the best way to do this.
    txt = ("\n{} {},\n\n {:>45}${:.2f}.\n\n {: >40}.\n\n{:>40}\n"
           "{:>42}".format(e_frmt.get(0), name, e_frmt.get(1), 
                           newAmout, e_frmt.get(2), e_frmt.get(3),
                           e_frmt.get(4)))
    return txt  # this way we can print to file


def send_ty_all():
    for personName in donor_db:
        # assuming that the last donation appended to last
        letter = email_template(personName, donor_db[personName][-1])
        textfile = personName.replace(" ", "_") + "_"+str(datetime.now())
        #made correction here based on Dirk comment
        textfile = textfile.replace(" ", "_")+".txt"
        with open(textfile, 'w') as file_object:
            file_object.write(letter)


# a better way to exit from Chris video
def exit_menu():
    print("\nExiting the menu.")
    return "Exit Menu"

# lesson learned - the value as function need to be below the defined function
# otherwise error - NameError 'send_ty' is not defined.
sub_menu_dict = {
                "list": list_donors,
                "1": update_donation,
                "q": exit_menu
                }

main_menu_dict = {
                "1": send_ty,
                "2": create_rpt,
                "3": send_ty_all,
                "q": exit_menu
                }


# for additional manual testing
def test_print_db():
    print(donor_db)

if __name__ == '__main__':
    # ask the intend of the comment in class
    # main()
    show_menu(promptText, main_menu_dict)
