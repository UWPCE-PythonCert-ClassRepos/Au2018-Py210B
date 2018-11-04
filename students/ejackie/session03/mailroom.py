#!/usr/bin/python

##################################################
## Author: Jackie Cheung
## Date: 2018/10/23
## Version: 0.1
## Class: Au2018-Py210B
## Description: Mailroom Part 1 - sending Thank You email and create report
##################################################

import sys  # imports go at the top of the file

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ]

prompt = "\n".join(("Welcome to the Mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Exit",
          ">>> "))

# Looking up the donor and add them to database if not exist
def send_a_thank_you(donor_db):
    name = input("Please enter the full name of the donor: ")
    if(name == "list"):
        for i, item in enumerate(donor_db):
            print(donor_db[i][0])
        print()
    else:
        for i, item in enumerate(donor_db):
            if name == donor_db[i][0]:
                amount = input("Please enter the amount of donation: ")
                donor_db[i][1].append(amount)
                send_email(name, amount)
            else:
                amount = input("Please enter the amount of donation: ")
                t = (name, amount)
                donor_db.append(t)
                send_email(name, amount)

# Sending a nicely formatted Thank you email
def send_email(name, amount):
    print('\n---------- Sending Thank You email ----------\n')
    print('{:5}{:70}'.format('Dear', name, ''))
    print()
    print('{:60}{:20}'.format('Thank you very much for your generous donation of: ', amount, ''))
    print()
    print('{:60}{:20}'.format('Your help is very appreciated. Have a wonderful day!', ''))
    print()
    print('{:60}{:20}'.format('Your Sincerely,', ''))
    print('{:60}{:20}'.format('The Mailroom', ''))
    print('\n---------- End of the email ----------\n')
    exit

# Creating a donation history report
def create_a_report():
    print('{:26}{:12}{:12}{:12}'.format('Donor Name', '| Total Given ', '| Num Gifts ', '| Average Gift'))
    print('------------------------------------------------------------------')
    for i, item in enumerate(donor_db):
        print('{:26}${:12.2f}{:^11}${:12.2f}'.format(donor_db[i][0], sum(donor_db[i][1]), len(donor_db[i][1]), sum(donor_db[i][1])/len(donor_db[i][1])))

# Exiting the program
def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_a_thank_you(donor_db)
        elif response == "2":
            create_a_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()