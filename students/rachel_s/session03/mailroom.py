#!/usr/bin/env python3

import csv

# Import donor data

donor_info = []
donor_names = []

def add_donation(db, name, amount):
    for item in db:
        if item[0] == name.lower():
            item[1].append(amount)

def add_new_donor(db, name, amount):
    db.append([name, [amount]])

def get_donor(db, name):
    for item in db:
        if item[0] == name.lower():
            return item

with open('donors.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        if not line[0].lower() in donor_names:
            donor_names.append(line[0].lower())
            add_new_donor(donor_info, line[0].lower(), int(line[1]))
        else:
            add_donation(donor_info, line[0], int(line[1]))

def user_menu():
    response = input("\nSelect an option:\n  1  Send a thank you\n  2  Create a report\n  3  Quit\n\n> ")
    if response == '1':
        send_thank_you()
    elif response == '2':
        create_report()
    elif response == '3':
        quit()
    else:
        response = input("Please select 1, 2, or 3.\n> ")

# Send a thank you
def send_thank_you():
    donor_name = input("What is the donor's full name?\n> ").lower()
    if donor_name == 'list':
        for i in donor_names:
            print(i)
    else:
        donation = int(input("Please enter the donation amount.\n> "))
        if donor_name in donor_names:
            add_donation(donor_info, donor_name, donation)
        else:
            add_new_donor(donor_info, donor_name, donation)
    my_donor = get_donor(donor_info, donor_name)
    
    thank_you_note = "Dear {name},\nThank you for your recent donation in the amount of ${amount:.2f}. You have donated {count} times for a total of ${total:.2f}! We will ensure that your contributions are put to good use defending the universe.\nSincerely,\nThe Bravest Warriors"
    print(thank_you_note.format(name=my_donor[0].title(), amount=donation, count=len(my_donor[1]), total=sum(my_donor[1])))
    user_menu()


# Create a report
def create_report():
    colnames = ["Donor Name", "Total Given", "Num Gifts", "Avg Gift"]
    title = "{:<21}| {:>13} |{:>13} |{:>14}".format(colnames[0], colnames[1], colnames[2], colnames[3])
    mystr = "{name:20} | ${total:>12.2f} | {count:>12} | ${avg:>12.2f}"
    print(title)
    print("---------------------|---------------|--------------|--------------")
    for item in donor_info:
        print(mystr.format(name=item[0].title(), total=sum(item[1]), count=len(item[1]), avg=(sum(item[1])/len(item[1]))))
    user_menu()

if __name__ == "__main__":
    user_menu()