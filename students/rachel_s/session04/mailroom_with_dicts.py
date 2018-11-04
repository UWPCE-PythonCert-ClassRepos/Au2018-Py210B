#!/usr/bin/env python3

import csv
import os
import datetime

# Import donor data

donor_info = {}

with open('mailroom/donors.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        if not line[0].lower() in donor_info:
            donor_info[line[0].lower()] = [int(line[1])]
        else:
            donor_info[line[0].lower()].append(int(line[1]))


def user_menu():
    menu = {1: send_thank_you, 2: create_report, 3: all_donor_letters, 4: quit}
    response = input("Select an option:\n  1  Send a thank you to a single donor\n  2  Create a report\n  3  Send letters to all donors\n  4  Quit\n\n> ")
    if int(response) in menu.keys():
        menu.get(int(response))()
    else:
        response = input("Please select 1, 2, 3, or 4.\n> ")


# Send a thank you
def send_thank_you():
    donor_name = input("What is the donor's full name?\n> ").lower()
    if donor_name == 'list':
        for i in donor_info.keys():
            print(i.title())
        user_menu()
    else:
        donation = int(input("Please enter the donation amount.\n> "))
        add_donor(donor_name, donation)
        print(generate_letter(donor_name))


def add_donor(name, amount):
    name = name.lower()
    if name in donor_info:
        donor_info[name].append(amount)
    else:
        donor_info[name] = [amount]


def generate_letter(donor):
    donor = donor.lower()
    name = donor.title()
    if len(donor_info.get(donor)) > 1:
        donation_count = len(donor_info.get(donor))
        donation_total = sum(donor_info.get(donor))
        middle = "You have donated {count} times for a total of ${total:.2f}! ".format(count=donation_count, total=donation_total)
    else:
        middle = "We greatly appreciate your generous contribution to our cause! "

    letter = "Dear {name},\nThank you for your recent donation in the amount of ${amount:.2f}. {middle} We will ensure that these funds are put to good use defending the universe.\nSincerely,\nThe Bravest Warriors"

    return letter.format(name=name, amount=donor_info.get(donor)[-1], middle=middle)


# Send thank you letters to all donors
def all_donor_letters():
    user_dir = input("What directory do you want to write to?\n\n>  ")
    dest = "{user_dir}/{date}_{name}.txt"
    date = datetime.datetime.today().strftime("%Y-%m-%d")
    if not os.path.isdir(user_dir):
        os.makedirs(user_dir)
    for name, donations in donor_info.items():
        path = dest.format(user_dir=user_dir, name=name, date=date)
        with open(path, "w") as f:
            f.write(generate_letter(name))


# Create a report
def create_report():
    colnames = ["Donor Name", "Total Given", "Num Gifts", "Avg Gift"]
    title = "{:<21}| {:>13} |{:>13} |{:>14}".format(colnames[0], colnames[1],
     colnames[2], colnames[3])
    mystr = "{name:20} | ${total:>12.2f} | {count:>12} | ${avg:>12.2f}"
    print(title)
    print("---------------------|---------------|--------------|--------------")
    for name, donations in donor_info.items():
        print(mystr.format(name=name.title(), total=sum(donations), count=len
        (donations), avg=(sum(donations)/len(donations))))
        print()
    user_menu()

if __name__ == "__main__":
    user_menu()