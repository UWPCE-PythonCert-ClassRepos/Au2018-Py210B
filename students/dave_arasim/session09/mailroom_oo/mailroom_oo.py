#!/usr/bin/env python
'''Object-oriented Mailroom User-interface for Session 9, Python 210
Written by David K. Arasim - 12/06/18'''

# Imported modules
import platform
import os
import io
from collections import defaultdict
from donor_models import *

# Global variables
this_os = platform.system()
quit_option = False

#############################################################################################
# Function section

def main():
    global quit_option

    # Build the Donor Dictionary (from a text file if it exists)
    donor_dict = DonorCollection('donors.txt')

    # Build the 'thank you' form letter text string
    build_form_text()

    # Build 'switch' dictionary for menu options
    switch_options = [1, 2, 3, 4]
    switch_functions = [send_thank_you, create_report, send_all_thanks, quit_option_true]
    switch_dict = {sw_opt: sw_fun for sw_opt, sw_fun in zip(switch_options, switch_functions)}

    while not quit_option:
        clear_screen()

        print('*'*10,'  Main Menu  ','*'*10)
        print()
        print('1) Send a Thank You to a single donor')
        print('2) Create a Report')
        print('3) Send Thank You letters to all donors')
        print('4) Quit')
        print()
        print('Choose an option: ', end='')

        user_choice = input()
        print()

        try:
            user_choice = int(user_choice)
        except ValueError:
            print('Sorry, but that is not a number')
        else:
            try:
                switch_dict.get(user_choice)(donor_dict)
            except TypeError:
                print('That option: ', user_choice, ' is out of range', sep='')

        print()

        if quit_option:
            print('Quitting process...')
        else:
            print('<cr> to continue... ', end='')
            input()  # input() for pause

    # Export the Donor Dictionary back to a text file
    donor_dict.build_donor_text()


def clear_screen():
    # Clear the screen based on operating system in use
    global this_os

    if this_os == 'Windows':
        os.system('clear')
    else:
        os.system('cls')


def quit_option_true(donor_dict):
    '''Set the quit_option to true (so function can be selected from switch_dict)'''
    global quit_option
    quit_option = True


def build_form_text():
    '''Build the 'thank you' form letter text string'''
    global form_text_str

    form_text = ['Dear {form_name},\n',
                 'Thank you for your generous donation of ${form_amt:.2f}\n',
                 'Please consider this e-mail as record of your donation for tax deduction purposes.\n',
                 'Sincerely, Your Local Charity']
    form_text_str = ''.join(x for x in form_text) # Comprehension
    return form_text_str


def send_thank_you(donor_dict):
    '''Sends thank you letter to single donor as their donation is made and recorded'''
    quit_thank_you = False

    clear_screen()

    while not quit_thank_you:
        print("Enter Donor's name, type 'list' for existing Donors (<cr> to exit): ", end='')

        donor_choice = input()
        print()

        if donor_choice == '': quit_thank_you = True
        elif donor_choice == 'list':
            print(donor_dict.generate_list(), sep='')
            print()
        else:
            donation_amt = find_donor(donor_dict, donor_choice)
            thank_donor(donor_choice, donation_amt)
            quit_thank_you = True


def find_donor(donor_dict, donor_choice, donation_amt = None):
    '''Finds an existing Donor OR installs a new Donor and records donation amount'''
    valid_amt = False

    while not valid_amt:
        if donation_amt is None:
            print('Please enter donation amount for ', donor_choice, ': $', sep='', end='')
            donation_amt = input()

        try:
            donation_amt = float(donation_amt)
        except ValueError:
            print('Sorry but that is not a valid amount')
            print()

            donation_amt = None
        else:
            valid_amt = True

    donor_dict.add_donation(donor_choice, donation_amt)

    return donation_amt


def thank_donor(donor_choice, donation_amt):
    '''Send a thank you letter to current Donor for current donation only'''
    print()
    print('E-mail form letter output:')
    print()
    print(build_form_text_out(donor_choice, donation_amt))
    print()
    print('End e-mail form letter output, <cr> to continue... ', end='')
    input()  # input() for pause


def build_form_text_out(form_name, form_amt):
    '''Builds form text output from form_text_str and its related format values'''
    global form_text_str

    form_dict = {'form_name': form_name, 'form_amt': form_amt}
    return form_text_str.format(**form_dict)


def send_all_thanks(donor_dict):
    '''Send thank you letters to all donors as text files named as donor_name.txt'''
    thank_you_list = donor_dict.build_thank_you_list()

    for donor_line in thank_you_list:
        this_name, this_amts = donor_line.split(':')
        this_tot = sum([float(amt) for amt in this_amts.split(',')])
        this_file = this_name.replace(' ', '_') + '.txt'

        with open(this_file, 'w') as thank_you_file:
            thank_you_file.write(build_form_text_out(this_name, this_tot))

        thank_you_file.close()

        print('Created Thank You letter: ', this_file)


def create_report(donor_dict):
    print(donor_dict.generate_report(), sep='')


#############################################################################################
# Main section

if __name__ == "__main__":
    # Guards against code running automatically if this module is imported
    main()
