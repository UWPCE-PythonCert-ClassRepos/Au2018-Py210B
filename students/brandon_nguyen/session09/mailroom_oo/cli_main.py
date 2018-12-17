#!/usr/bin/env python3
# Week9 Excercise cli_main.py
# Student: Brandon Nguyen - Au2018


import unittest
import os
from os import makedirs

from donor_model import *


db = DonorCollection()


def create_files(in_list):
    """ This function is to create letters from a list of stuple
    :parma in_list = [("letter content", fileName),]
    """
    for i in range(len(in_list)):
        with open(in_list[i][1], 'w') as file_object:
            file_object.write(in_list[i][0])


def send_all_letters():
    create_files(db.ty_letter_all())


def create_rpt_donor():
    """ This will only create a report for a donor """
    input_person = input("\nPlease enter donor full names: ")
    if input_person in db.list_donors():
        print("\n\n")
        print(db.list_rpt_data(input_person))
    else:
        print("\n\nSORRY!!!  That donor do not exist!")


def create_rpt():
    """
    This function is to print the report of donors.
    """
    if len(db.list_donors()) >= 1:
        print("\n\n")
        print(db.list_rpt_data())
    else:
        print("\nSORRY.  We do not have any donor available for report!\n")


# all Done for oo.
def show_menu(promptxt, select_dict):
    while True:
        try:
            menu_selected = input(promptxt)
            if select_dict[menu_selected]() == 'Exit Menu':
                break
        except KeyError as err:
            print()
            print("You entered: {} incorrect option!".format(err))


def update_donation_call():
    """
    This func update the DonorCollection with input.
    """
    input_person = input("\nPlease enter donor full names: ")
    while True:
        try:
            input_donation = float(input("Please enter donation amount for " +
                                   input_person + ":>> "))
            break
        except ValueError:
            print("\nPlease Reenter amount in float.")
    db.add_donor_db(input_person.strip(), input_donation)
    donor = db.get_donor_data(input_person.strip())
    print(donor.ty_letter())


def exit_menu():
    print("\nExiting the menu.")
    return "Exit Menu"


def list_donors():
    """
    Basic Name of donor return in Order by First Name
    """
    if len(db.list_donors()) >= 1:
        for name in db.list_donors():
            print(name)
    print("\nSORRY.  We do not have any donor available!\n")


def send_ty():
    subMenuPrompt = ("Please Chose an option:\n\nlist - "
                     "To display a list of current donors.\n"
                     "1    - To enter name of donor to update.\n"
                     "2    - To create a report for a donor.\n"
                     "q    - To exit this menu.\n"
                     ">>> ")

    sub_menu_dict = {
                    "list": list_donors,  # Done in oo
                    "1": update_donation_call,  # Done in oo
                    "2": create_rpt_donor,  # Done in oo
                    "q": exit_menu  # done for oo
                    }
    show_menu(subMenuPrompt, sub_menu_dict)


def main():
    """main to involke all menus"""
    promptText = "\n".join(("\nWelcome to the mailroom program!\n",
                            "Please choose an options:\n\n",
                            "1 - Add Donation and send Thank You to a donor.",
                            "2 - Create a Report.",
                            "3 - Send letters to all donors.",
                            "q - Quit",
                            ">>> "))

    main_menu_dict = {
                    '1': send_ty,  # Done
                    '2': create_rpt,  # Done
                    '3': send_all_letters,  # Done
                    'q': exit_menu  # Done
                    }

    show_menu(promptText, main_menu_dict)

if __name__ == "__main__":
    main()
