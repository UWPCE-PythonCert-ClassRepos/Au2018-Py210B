
import sys

user_menu = "\n".join(("Would you like to: ",
"1 - Send a Thank You",
"2 - Create a Report",
"3 - Quit",
">>>> "))

donor_db = [
("Alex", [53898.23, 2653.00, 105.07]) ,
("Jeff", [183.00, 200.00]) ,
("Paul", [33941.98]) ,
("Mark", [1.65, 55.00]) ,
("John", [2705.71])]

def sort_key(donor_db):
    return sum(donor_db[1])

def send_thanks():
    name = ''
    while not name or name.lower() == 'list':
        name = input("Please enter the full name: ")
        if name.lower() == 'list':
            print(' '.join(x[0] for x in donor_db))

    donation = int(input("Please enter the donation amount: "))
    for i in range(len(donor_db)):
        if name.lower() ==  donor_db[i][0].lower():
            donor_db[i][1].append(donation)
            return
    donor_db.append((name, [donation]))

    print("\nDear {},".format(name))
    print("\nThank you for the donation of ${}".format(donation))
    print("\nSincerely,")
    print("The Mailroom Foundation\n\n")


def donor_rpt():
    print('\n\n')
    print('{:13}|{:^10}|{:^10}|{:^10}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-' * 50)

    sorted(donor_db, key=sort_key, reverse=True)

    for i in donor_db:
        print(f'{i[0]:13}', f'${sum(i[1]):>10.2f}', f'{len(i[1]):>10}', f'${(sum(i[1])/len(i[1])):>10.2f}')

def exit_program():
    print("Bye!")
    sys.exit() 

def main():
    while True:
        response = input(user_menu)
        if response == "1":
            send_thanks()
        elif response == "2":
            donor_rpt()
        elif response == "3":
            exit_program()
        else:
            print("Warning: Not a valid option!")

if __name__ == "__main__":
    main()
