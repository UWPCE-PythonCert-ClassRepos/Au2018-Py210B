#!/usr/bin/env python
'''Mailroom Part 2 for Session 4, Python 210
Written by David K. Arasim - 10/28/18'''

#Imported modules
import platform
import os
from collections import defaultdict

#Global variables
this_os = platform.system()
quit_option = False

#############################################################################################
#Function section

def main():
    global this_os
    global quit_option

    donor_dict = defaultdict(list)
    build_donor_dict(donor_dict)    #Build the Donor Dictionary from a text file

    switch_dict = {1: send_thank_you, 2: create_report, 3: send_all_thanks, 4: quit_option_true}

    while not(quit_option):
        if this_os == 'Windows':
            os.system('clear')
        else:
            os.system('cls')

        print ('*'*10,'  Main Menu  ','*'*10)
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
            user_choice = ''

        if user_choice == '':
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
            cont_input = input()  #cont_input for pause (variable not used)

    build_donor_text(donor_dict)  #Export the Donor Dictionary back to a text file

def quit_option_true(donor_dict):
    '''Set the quit_option to true, so function can be selected from dict switch'''
    global quit_option
    quit_option = True

def build_donor_dict(donor_dict):
    '''Build Donor Dictionary by extracting values from a text file'''
    try:
        with open('donor_dict.txt', 'r') as dictfile:
            while True:
                donor_dict_line = dictfile.readline()
                if not donor_dict_line: break

                donor_dict_line = donor_dict_line.strip()
                donor_dict_name = donor_dict_line.split(':')[0]
                donor_dict_amts = donor_dict_line.split(':')[1].split(',')

                for amts in donor_dict_amts:
                    donor_dict[donor_dict_name].append(float(amts))

        dictfile.close()
    except FileNotFoundError:
        print()
        print('Donor database in donor_dict.txt not found.  Starting with new, empty database.')
        print()

def build_donor_text(donor_dict):
    '''Export the Donor Dictionary date back to a text file'''
    with open('donor_dict.txt', 'w') as dictfile:
        for this_name, this_amts in donor_dict.items():
            amts_str  = ','.join(str(x) for x in this_amts)
            this_line = this_name + ':' + amts_str + '\n'

            dictfile.write(this_line)

    dictfile.close()

def send_thank_you(donor_dict):
    '''Sends thank you letter to single donor as their donation is made and recorded'''
    global this_os
    quit_thank_you = False

    if this_os == 'Windows':
        os.system('clear')
    else:
        os.system('cls')

    while not(quit_thank_you):
        print("Enter Donor's name, type 'list' for existing Donors (<cr> to exit): ", end='')

        thank_you_choice = input()
        print()

        if   thank_you_choice == '':     quit_thank_you = True
        elif thank_you_choice == 'list': show_donor_list(donor_dict)
        else:
            find_donor(donor_dict, thank_you_choice)
            quit_thank_you = True

def show_donor_list(donor_dict):
    '''Show the Donor List of names only'''
    donor_list   = 'List of Donors'
    donor_list_w = 26

    #Donor list header
    list_nom = (donor_list, donor_list_w)
    print('{:{}}'.format(*list_nom))
    print('-'*donor_list_w)
    
    #Donor list body
    for this_name in donor_dict:
        #Data line
        this_line = (this_name, donor_list_w)
        print('{:{}}'.format(*this_line))

    print()

def find_donor(donor_dict, thank_you_choice):
    '''Finds an existing Donor OR installs a new Donor and records donation amount.
	It then sends a thank you letter to that Donor for the current donation.'''
    print('Please enter donation amount for ', thank_you_choice, ': $', sep='', end='')
    donation_amt = float(input())

    donor_dict[thank_you_choice].append(donation_amt)

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

def send_all_thanks(donor_dict):
    '''Send thank you letters to all donors as text files named as donor_name.txt'''
    for this_name, this_amts in donor_dict.items():
        thank_you_text = ''

        this_tot  = sum(this_amts)
        this_file = this_name.replace(' ', '_') + '.txt'

        thank_you_text += 'Dear {},'.format(this_name) + '\n'
        thank_you_text += 'Thank you for your generous donation of ${:.2f}'.format(this_tot) + '\n'
        thank_you_text += 'Please consider this e-mail as record of your donation for tax deduction purposes.' + '\n'
        thank_you_text += 'Sincerely, Your Local Charity'

        with open(this_file, 'w') as thank_you_file:
            thank_you_file.write(thank_you_text)

        thank_you_file.close()

        print('Created Thank You letter: ', this_file)

def create_report(donor_dict):
    '''Show report of Donor Names and their donation summary: Total Given|Number of Gifts|Average Gift Amount'''
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
    for this_name, this_amts in donor_dict.items():
        this_tot = sum(this_amts)
        this_cnt = len(this_amts)

        #Avoid division by zero
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