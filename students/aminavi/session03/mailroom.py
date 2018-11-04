import sys


donor_list = [('William',[ 653772.32 , 953772.32,100000]),('Jeff', [ 8888777.22 ,877.33 ]),('Paul', [663.23, 43.87 ,1.32 ]),('Mark', [1663.23, 4300.87, 10432.00]),('Nigel',[5000000 , 10])]

thank_you_action = "Send a Thank You"
create_a_report = "Create a Report"
quit_action = "quit"

def send_thank_you():
    name = ''
    while not name or name.lower() == 'list':
        name = input("Please enter the full name: ")
        if name.lower() == 'list':
            print(' '.join(x[0] for x in donor_list))

    donation = int(input("Please enter the donation amount: "))
    for i in range(len(donor_list)):
        if name.lower() ==  donor_list[i][0].lower():
            donor_list[i][1].append(donation)
            return
    donor_list.append((name, [donation]))

    print("\nDear {},".format(name))
    print("Thank you for your generous donation of ${}".format(donation))
    print("You have our sincere gratitude.\nThank you\n\n")


def sum_donations(donations):
    total = 0
    for d in donations:
        total += d
    return total


def create_report():
    print('\n\n')
    print('{:<25}|{:^17}|{:^15}|{:^17}'.format('Donor Name','Total Given','Num Gifts', 'Average Gift'))
    print(75 * '-')
    result = [(x[0], [sum_donations(x[1]), len(x[1]), sum_donations(x[1])/len(x[1])])
                for x in donor_list]
    result = sorted(result, key=lambda item: item[1][0], reverse=True)
    for y in result:
        print("{:<25} ${:15.2f}{:16}  ${:14.2f}".format(y[0],
                                        y[1][0],
                                        y[1][1],
                                        y[1][2]))
    print('\n\n')


if __name__ == '__main__':
    prompt = ("Select an action: \n1.{}\n2.{}\n3.{}\n".format(thank_you_action, create_a_report, quit_action))
    while True:
        response = input(prompt)  # continuously collect user selection
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            print('Bye')
            sys.exit()
        else:
            print("Not a valid option!")
