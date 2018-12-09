#!/usr/bin/env python

""" Mailroom_oo Main menu, including input and output """

from donor_models import *

donor_database = DonorCollection()


def update_donor_donation():
    """ Identifies selection as update and not new donor """
    donor_donation(True)


def donor_donation(update_donor=False):
    """ Adds new donor to the donorDB or updates existing """

    while True:
        name = input("Please enter full name or list> ")
        if name == "":
            print("Please enter valid name.\n")
        elif name == "list":
            print('\n'.join(donor_database.collect_data()))
        elif update_donor and not donor_database.search_name(name):
            print("Name not found in donor records.")
        else:
            goforward = input("Is \"{}\" the correct name (Y/N)? ".format(name))
            if goforward in ["y", "Y"]:
                while True:
                    donationamount = input("Enter donation amount> ")
                    if donor_database.donor_update(name, donationamount):
                        # print thankyou letter, float will work if donor_upate was True
                        printthankyou(name, float(donationamount))
                        break
                    print("Please enter a valid donation.")
                break


def printreport():
    """ Prints report created in the class """

    print(donor_database.create_report())
    print()


def printthankyou(name, donationamount):
    """Prints the thank you letter to standard output
    :param donorname: the index to the donor in the database the letter should
                    be addressed too
    """

    print(donor_database.THANK_YOU_LETTER.format(name=name, amount=donationamount))


def writeallletters():
    """ Write a letter to a file for each donor. """

    if donor_database.write_letters():
        print("Letters written to files.\n")
    else:
        print("Failure to write letters.\n")


def exit_program():
    """Prints good bye and returns exit to end the loop"""

    print("Thank you. Bye")
    return "exit"


def main():
    """ Mailroom_oo main program loop with menu """

    menudict = {
        '1': donor_donation,
        '2': update_donor_donation,
        '3': printreport,
        '4': writeallletters,
        '5': exit_program}

    mainmenu = "\n".join(("Welcome to the mailroom!",
                          "Please choose from below options:",
                          "1 - Add new donor to database",
                          "2 - Add donation to existing donor",
                          "3 - Create a Report",
                          "4 - Send letters to all donors",
                          "5 - Quit",
                          ">>> "))

    while True:
        choice = input(mainmenu)

        try:
            if menudict.get(choice)() == "exit":
                break
        except TypeError as e:
            print("\nPlease enter a valid menu choice.\n")
            print(e)


if __name__ == "__main__":

    main()
