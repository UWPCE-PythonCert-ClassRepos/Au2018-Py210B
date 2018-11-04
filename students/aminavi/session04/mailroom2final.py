import sys
import tempfile

donor_list = {
    'william': [653772.32 , 953772.32,100000],
    'jeff': [8888777.22 ,877.33],
    'paul': [663.23, 43.87 ,1.32],
    'mark': [1663.23, 4300.87, 10432.00],
    'nigel': [5000000 , 10]
    }


def send_thank_you():
    name = ''
    while not name or name.lower() == 'list':
        name = input("Please enter the full name: ")
        if name.lower() == 'list':
            print(''.join(donor_list))
    donation = int(input("Please enter the donation amount: "))
    donor_list.setdefault(name.lower(),[]).append(donation)

    print("\nDear {},".format(name))
    print("Thank you for your generous donation of ${}".format(donation))
    print("You have our sincere gratitude.\nThank you\n\n")

def create_a_report():
    print('\n\n')
    print('{:<25}|{:^17}|{:^15}|{:^17}'.format('Donor Name','Total Given','Num Gifts', 'Average Gift'))
    print(75 * '-')
    sorted_donor_list = sorted(donor_list, key=donor_list.get, reverse=True)
    for key in sorted_donor_list:
        print(f'{key:25}', f'${sum(donor_list[key]):>17.2f}', f'{len(donor_list[key]):^15}', f'${(sum(donor_list[key])/len(donor_list[key])):>17.2f}')


def thank_you_action_all():
    path = input("please enter the path ")
    if path != '':
        path = path + "\\"
    for k,v in donor_list.items():
        with open("{}{}.txt".format(path, k), "w") as letter:
            letter.write("Dear {},\n\n".format(k))
            letter.write("\tThank you for your generous donation of ${}\n\n".format(sum(v)))
            letter.write("\tIt will be put to very good use.\n\n")
            letter.write("\t\tSincerely,\n")
            letter.write("\t\t  - Team\n")
    
    if path != '':
        print("\n\nLetters were saved in {}.\n\n".format(path))
    else:
        print("\n\nletters were saved in the current directory.\n\n")


def quit_action():
    print('bye')
    sys.exit()


function_list = { 
    1: send_thank_you, 
    2: create_a_report, 
    3: thank_you_action_all,
    4: quit_action
}

actions = {"send": "Send a Thank You to a single donor.", 'create': "create a report. ", "all": "Send letters to all donors.", 'quit': "quit program"}


def Main():
    prompt = ("Choose an action: \n \n1 - {send}\n2 - {create}\n3 - {all}\n4 - {quit}\n".format(**actions))
    while True:
        response = int(input(prompt))
        if response in function_list.keys():
            function_list.get(response)()
        else:
            print("Not a valid option!")

if __name__ == '__main__':
   Main()