#Mailroom Part 2
import sys

#donor_db definition and default values

donor_db = {"John Smith": [500.00, 150.00, 20.00],
            "Jane Doe": [340.00, 30.00, 200.00],
            "Jason Bourne": [240.00, 140.00],
            "John Wick": [1000.00],
            "GI Jane": [150.00, 60.00]
            }


#Thank you letter template
thankyouletter = "\n".join(("","Dear {name},","","Thank you for your generous donation of ${amount:.2f} to our cause.","Your donations help keep Python great!","","Sincerely","","The Python Project",""))

def sumdbkey(donorlist):
    """Used by function sortdb to generate sort key
    :param donorlist: iterate through donordb tuples
    """
    return sum(donorlist[1])

def sortdb():
    """Returns a new db sorted on the sum of donations"""
    return sorted(donor_db.items(), key=sumdbkey, reverse=True)

def printthankyou(donorname):
    """Prints the thank you letter to standard output
    :param donoridx: the index to the donor in the database the letter should be addressed too
    """
    print(thankyouletter.format(name=donorname, amount=donor_db[donorname][-1]))

def adddonation(donorname):
    """Gets donation amount from user and adds it to the donor's entry in db
    :param donoridx: the index to the donor in the database that the donation should be added too
    """
    donationammount = input("Enter donation amount> ")
    donor_db[donorname].append(float(donationammount))

def printdonorlist():
    """Prints a list of all donors in the db"""
    for name in donor_db.keys():
        print(name)

def handlename(namechoice):
    """Determines if name provided is existing donor or new donor. Calls function to add donation to DB and calls function to print thank you letter
    :param namechoice: name of the donor entered by user
    """
    #getting the name index starting from 1 to use truthiness in if statement
    if namechoice in donor_db:
        adddonation(namechoice)
        printthankyou(namechoice)
    else:
        donor_db[namechoice] = []
        adddonation(namechoice)
        printthankyou(namechoice)


def printreport():
    """Obtains new sorted DB and prints report"""
    newdb = sortdb()
    print()
    print("{:<26}|{:^13}|{:^11}|{:^14}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("{:-<67}".format(""))
    for name, donation in newdb:
        print("{:<27}${:>11.2f} {:>11d}  ${:>12.2f}".format(name, sum(donation), len(donation), sum(donation)/len(donation)))
    print()

def exit_program():
    print("Thank you. Bye")
    #print(donor_db)
    sys.exit()

def main():
    """Mailroom main program loop with menu"""

    menu = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

    while True:
        choice = input(menu)
        if choice == '1':
            name = input("Please enter full name or list> ")
            if name == "list":
                printdonorlist()
            else:
                handlename(name)
        elif choice == '2':
            printreport()
        elif choice == '3':
            exit_program()
        else:
            print("Incorrect Entry\n")

if __name__ == "__main__":
    main()
