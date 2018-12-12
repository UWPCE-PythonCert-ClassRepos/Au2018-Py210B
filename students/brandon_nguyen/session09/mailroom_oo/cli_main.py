#!/usr/bin/env python3
# Week9 Excercise cli_main.py
# Student: Brandon Nguyen - Au2018

from donor_model import *


db = DonorCollection()

# TODO
    # 1) The two funtions below
    # 2


def send_all_letters():
    pass


def create_rpt():
    """
    This function is to print the report of donors.
    """
    pass


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
    donor = db.get_name(input_person.strip())
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
    print("SORRY.  We do not have any donor available!\n")


def send_ty():
    subMenuPrompt = ("Please Chose an option:\n\nlist - "
                     "To display a list of current donors.\n"
                     "1    - To enter name of donor to update.\n"
                     "q    - To exit this menu.\n"
                     ">>> ")

    sub_menu_dict = {
                    "list": list_donors,  # Done in oo
                    "1": update_donation_call,  # Done in oo with only new.
                    "q": exit_menu  # done for oo
                    }
    show_menu(subMenuPrompt, sub_menu_dict)


def main():
    """main to involke all menus"""
    promptText = "\n".join(("\nWelcome to the mailroom program!\n",
                            "Please choose an options:\n\n",
                            "1 - Send a Thank You to a single donor.",
                            "2 - Create a Report.",
                            "3 - Send letters to all donors.",
                            "q - Quit",
                            ">>> "))

    main_menu_dict = {
                    '1': send_ty,  # Done
                    '2': create_rpt,  # TODO
                    '3': send_all_letters,  # TODO
                    'q': exit_menu  # Done
                    }

    show_menu(promptText, main_menu_dict)

if __name__ == "__main__":
    main()
