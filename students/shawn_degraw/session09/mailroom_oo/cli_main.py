#!/usr/bin/env python

""" Mailroom_oo Main menu, including input and output """

from donor_models import *

donor_database = DonorCollection()


def newdonor_donation():
    """ Adds new donor to the donorDB or updates existing """

    while True:
        name = input("Please enter full name or list> ")
        if name == "":
            print("Please enter valid name.\n")
        elif name == "list":
            print(donor_database.collect_data())
        else:
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


def printthankyou(name, donationamount):
    """Prints the thank you letter to standard output
    :param donorname: the index to the donor in the database the letter should
                    be addressed too
    """
    print(donor_database.THANK_YOU_LETTER.format(name=name, amount=donationamount))


def writeallletters():
    """ Write a letter to a file for each donor. """

    for name in donor_database.collect_data():
        filename = name.replace(' ', '_') + ".txt"

        formatdict = {"name": name, "totaldonation": donor_database.search_name(name).totaldonations / 100}
        try:
            with open(filename, 'w') as outfile:
                outfile.write(donor_database.GENERAL_DONATION_LETTER.format(**formatdict))
        except IOError:
            print("Error: Cannot create letters.")
            break


def exit_program():
    """Prints good bye and returns exit to end the loop"""

    print("Thank you. Bye")
    return "exit"


def main():
    """ Mailroom_oo main program loop with menu """

    menudict = {
        '1': newdonor_donation,
        '2': newdonor_donation,
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
