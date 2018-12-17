#!/usr/bin/env python3

##################################################
# Author: Jackie Cheung
# Date: 2018/11/06
# Version: 0.1
# Class: Au2018-Py210B
# Description: Mailroom Part 3 - Improve your mailroom by adding exceptions and comprehensions
##################################################

import sys  # imports go at the top of the file

def menu_selection(prompt, dispatch_dict):
    while True:  # loop forever until they quit.
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "exit program":
                break
        except KeyError:
            print("Please choose a correct number!\n")


def list_donors():
    return [" ".join(key) for key in donor_dict]


def send_a_thank_you():
    name = input("Please enter the full name of the donor: ")
    if name == "list":
        #[print(" ".join(key)) for key in donor_dict]
        #print(list_donors())
        print("\n".join(list_donors()))
        print()
    elif tuple(name.split()) in donor_dict:
        print("Adding donation to existing donor")
        try:
            amount = float(input("Please enter the amount of donation: "))
        except ValueError:
            print("The amount entered is invalid! Please try again later.\n")
            return None
        donor_dict[tuple(name.split())].append(amount)
        print(send_email(name, amount))
    else:
        print("Adding new donor entry to the db")
        try:
            amount = float(input("Please enter the amount of donation: "))
        except ValueError:
            print("The amount entered is invalid! Please try again later.\n")
            return None
        donor_dict[tuple(name.split())] = [amount]
        print(send_email(name, amount))


# Creating a nicely formatted Thank you email as String
def send_email(name, amount):
    email = ('Dear {},'.format(name) + 
             '\n\n\tThank you for your very kind donation of ${:,.2f}.'.format(amount) + 
             '\n\n\tIt will be put to very good use.'
             '\n\n\t\tSincerely,'
             '\n\t\t   -The Mailroom'
             )
    return email


# Creating a donation history report
def create_a_report():
    report = ['{:23} | {:10} | {:8} | {:10}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'),
             '----------------------------------------------------------------']
    for key, value in donor_dict.items():
        report.append('{:24} ${:12.2f}{:12} ${:12.2f}'.format(' '.join(key), sum(value), len(value), sum(value)/len(value)))
    #[print('{:24} ${:12.2f}{:12} ${:12.2f}'.format(' '.join(key), sum(value), len(value), sum(value)/len(value))) for key, value in donor_dict.items()]
    #print()
    return '\n'.join(report)

def print_a_report():
    print(create_a_report())
    print()

# Creating a text letter file for all donors
def send_letters_to_all():
    print("Creating text file letter for all donors")
    for key, value in donor_dict.items():
        filename = '_'.join(key) + '.txt'
        try:
            with open(filename, 'w') as f:
                f.write(send_email(' '.join(key), sum(value)))
        except IOError:
            print("Not able to write files! Please try again later.")
            return None


# Exiting the program
def exit_program():
    print("Bye! Have a wonderful day!")
    sys.exit()  # exit the interactive script
    #return "exit program"


# Main menu selection
main_dispatch = {"1": send_a_thank_you,
                 "2": print_a_report,
                 "3": send_letters_to_all,
                 "4": exit_program,
                 }

donor_dict = {("William", "Gates", "III"): [653772.32, 12.17],
              ("Mark", "Zuckerberg"): [1663.23, 4300.87, 10432.0],
              ("Jeff", "Bezos"): [877.33],
              ("Paul", "Allen"): [663.23, 43.87, 1.32]
              }

main_prompt = "\n".join(("Welcome to the Mailroom!",
                         "Choose an action:",
                         "1 - Send a Thank You to a single donor",
                         "2 - Create a Report",
                         "3 - Send letters to all donors",
                         "4 - Quit",
                         ">>> "))


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
