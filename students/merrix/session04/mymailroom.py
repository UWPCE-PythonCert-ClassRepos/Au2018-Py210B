import sys  # imports go at the top of the file
from collections import defaultdict
from operator import itemgetter

donor_db = defaultdict(list)


donor_db = {"William Gates":[653772, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen" : [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]
           }

prompt = "\n".join(("Welcome to James Dot Donations!",
          "Please choose from below options:",
          "1 - Send a Thank you",
          "2 - Create a report",
          "3 - Send Letter",
          "4 - To Exit",
          ">>> "))


def view_donor_db():
    print (donor_db.keys())
    choose = input("enter a name from the list or a new name to donate: ").title()
    if choose not in donor_db.keys():
        add_donor_db(choose)
    elif choose in donor_db.keys():
        donation = int(input("Enter an amount to donate to %s " % choose)) 
        donor_db[choose].append(int(donation))
        print (donor_db)
        print ('''
        Thank you %s for your donation of $%i to this organization. 
        We really appreciate your generousity and hope to see you again at our upcoming events.
        Sincerely Yours
        James Dot
        ''' % (choose, donation))




def add_donor_db(choose):
    new_donor = input("Do you want to add %s to the donation list? yes or no " % choose).title()
    if new_donor == "Yes":
        amount = input("Enter an amount to donate for %s " % choose)
        donor_db.update({new_donor:amount})
        print (donor_db)
        print ('''
            Thank you %s for your donation of $%i to this organizat1ion. We really appreciate your generousity and hope to see you again at our upcoming events.
            Sincerely Yours
            James Dot
            ''' % (new_donor, int(amount)))





def user_Report():
    print('Donor Name  | ',  'Total Given | ', 'Num Gift  | ', 'Average Gift')
    for name, donations in donor_db.items():
        num_of_gift = len(donations)
        total_given = int(sum(donations))
        average_gift = int(total_given/num_of_gift)
        print ('{0:<15}   {1:^10}     {2:^6}     {3:8}'.format(name, total_given, num_of_gift, average_gift))
        

def send_letters():
    for donor_name in donor_db:
        letter = open('{}.txt'.format(donor_name), "w+")
        email_letter = '''Hello %s,
          Thank you for your donation to the organization, this is a thank you emailto show our appreciation.
          ''' % (donor_name)
        letter.write(email_letter)




def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            view_donor_db()
        elif response == "2":
            user_Report()
        elif response == "3":
            send_letters()
        elif response == "4":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()