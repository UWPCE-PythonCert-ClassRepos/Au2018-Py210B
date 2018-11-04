#!/usr/bin/env python
'''Mailroom Part 1 for Session 3, Python 210
Written by David K. Arasim - 10/22/18'''

#Imported modules
import os

#Global variables
donor_db = [("Bill Gates", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.00]),
            ("Richard Branson", [20000.00, 25000.00, 42.34])
            ]

#############################################################################################
#Function section

def main():
    quit_option = False

    while not(quit_option):
        os.system('clear')
        print ('*'*10,'  Main Menu  ','*'*10)
        print()
        print('1) Send a Thank You')
        print('2) Create a Report')
        print('3) Quit')
        print()
        print('Choose an option: ', end='')

        user_choice = input()
        print()

        try:
            user_choice = int(user_choice)
        except ValueError:
            user_choice = ''

        if user_choice == '':
            print('Sorry, but that is not a number')
        else:
            if   user_choice == 1: send_thank_you()
            elif user_choice == 2: create_report()
            elif user_choice == 3: quit_option = True
            else:
                print('That option: ', user_choice, ' is out of range', sep='')

        print()
        if quit_option:
            print('Quitting process...')
        else:
            print('<cr> to continue... ', end='')
            cont_input = input()  #cont_input for pause (variable not used)

def send_thank_you():
    quit_thank_you = False
    os.system('clear')

    while not(quit_thank_you):
        print("Enter Donor's name, type 'list' for existing Donors (<cr> to exit): ", end='')

        thank_you_choice = input()
        print()

        if   thank_you_choice == '':     quit_thank_you = True
        elif thank_you_choice == 'list': show_donor_list()
        else:
            find_donor(thank_you_choice)
            quit_thank_you = True

def show_donor_list():
    donor_list   = 'List of Donors'
    donor_list_w = 26

    #Donor list header
    list_nom = (donor_list, donor_list_w)
    print('{:{}}'.format(*list_nom))
    print('-'*donor_list_w)
    
    #Donor list body
    for this_donor in range(len(donor_db)):
        this_name = (donor_db[this_donor])[0]

        #Data line
        this_line = (this_name, donor_list_w)
        print('{:{}}'.format(*this_line))

    print()

def find_donor(thank_you_choice):
    for this_donor in range(len(donor_db)):
        this_name = (donor_db[this_donor])[0]

        if thank_you_choice == this_name:
            break
    else:
        donor_db.append((thank_you_choice, []))
        this_donor += 1

    print('Please enter donation amount for ', thank_you_choice, ': $', sep='', end='')
    donation_amt = float(input())

    ((donor_db[this_donor])[1]).append(donation_amt)

    print()
    print('E-mail form letter output:')
    print()
    print('Dear {},'.format(thank_you_choice))
    print('Thank you for your generous donation of ${:.2f}'.format(donation_amt))
    print('Please consider this e-mail as record of your donation for tax deduction purposes.')
    print('Sincerely, Your Local Charity')
    print()
    print('End e-mail form letter output, <cr> to continue... ', end='')
    cont_input = input()  #cont_input for pause (variable not used)

def create_report():
    donor_name = 'Donor Name'
    tot_given  = 'Total Given'
    num_gifts  = 'Num Gifts'
    avg_gift   = 'Average Gift'
    sep_char   = '|'

    donor_name_w = 26
    tot_given_w  = 13
    num_gifts_w  = 11
    avg_gift_w   = 13
    sep_char_w   = len(sep_char)

    #Report header
    header_nom = (donor_name, donor_name_w, sep_char, tot_given, tot_given_w, sep_char, num_gifts, num_gifts_w, sep_char, avg_gift, avg_gift_w)
    print('{:{}}{}{:>{}}{}{:>{}}{}{:>{}}'.format(*header_nom))
    print('-'*donor_name_w, '-'*sep_char_w, '-'*tot_given_w, '-'*sep_char_w, '-'*num_gifts_w, '-'*sep_char_w, '-'*avg_gift_w, sep='')

    #Report body
    for this_donor in range(len(donor_db)):
        this_name = (donor_db[this_donor])[0]
        this_tot  = sum((donor_db[this_donor])[1])
        this_cnt  = len((donor_db[this_donor])[1])

        if this_cnt != 0:
            this_avg = this_tot / this_cnt
        else:
            this_avg = 0

        #Data line
        this_line = (this_name, donor_name_w, this_tot, (tot_given_w - 1), this_cnt, num_gifts_w, this_avg, (avg_gift_w - 1))
        print('{:{}} ${:{}.2f} {:{}} ${:{}.2f}'.format(*this_line))

#############################################################################################
#Main section

if __name__ == "__main__":
    #Guards against code running automatically if this module is imported
    main()