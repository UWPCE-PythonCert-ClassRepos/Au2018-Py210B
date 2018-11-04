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

generaldonationletter ="\n".join(("","Dear {name},","","Thank you for your generosity in supporting us with ${totaldonation:.2f} in donations.", "We hope to have your continued support.", "","With great thanks", "", "The Python Project"))

def sumdbkey(donorlist):
    """Used by function sortdb to generate sort key
    :param donorlist: iterate through donordb tuples
    """
    return sum(donorlist[1])

def sortdb():
    """Returns a new db sorted on the sum of donations"""
    return sorted(donor_db.items(), key=sumdbkey, reverse=True)

def printthankyou(donorname):
    """Prints the thank you letter to standard output in mailroom part 1 format
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

def handlenames():
    """Determines if name provided is existing donor or new donor. Calls function to add donation to DB and calls function to print thank you letter"""

    name = input("Please enter full name or list> ")
    if name == "list":
        printdonorlist()
    #getting the name index starting from 1 to use truthiness in if statement
    elif name in donor_db:
        adddonation(name)
        printthankyou(name)
    else:
        donor_db[name] = []
        adddonation(name)
        printthankyou(name)


def printreport():
    """Obtains new sorted DB and prints report"""
    newdb = sortdb()
    print()
    print("{:<26}|{:^13}|{:^11}|{:^14}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("{:-<67}".format(""))
    for name, donation in newdb:
        print("{:<27}${:>11.2f} {:>11d}  ${:>12.2f}".format(name, sum(donation), len(donation), sum(donation)/len(donation)))
    print()

def sendletters():
    """Write a letter to a file for each donor. Letters put in Windows subdirectory called letters."""

    for donorname in donor_db:
        filename = "letters\\" + donorname.replace(' ', '_') + ".txt"
        #create a new dictionary just for the format mailroom part 2
        formatdict = {"name": donorname, "totaldonation": sum(donor_db[donorname])}
        with open(filename, 'w') as outfile:
            outfile.write(generaldonationletter.format(**formatdict))
    print("\nLetters printed to files.\n")

def exit_program():
    print("Thank you. Bye")
    #print(donor_db)
    return "exit"

def main():
    """Mailroom main program loop with menu"""

    menudict = {
            '1': handlenames,
            '2': printreport,
            '3': sendletters,
            '4': exit_program
    }

    mainmenu = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - Quit",
          ">>> "))

    while True:
        choice = input(mainmenu)

        if menudict.get(choice)() == "exit":
            break



if __name__ == "__main__":
    main()
