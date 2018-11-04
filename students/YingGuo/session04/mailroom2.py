#!/usr/bin/env python3

"""session04, assignment mailroom2, Ying Guo"""

from collections import defaultdict

data =defaultdict(list, {"Tom":[100,200], "Tim":[3000], "Ken": [888,888,888], "Ted":[8000,5000,500], "Jon":[1000,6000]})

#Send a thank you function 
def thank_you(data):
	while True:
		user_input = input("please enter the name of donor. You can enter list to see the exisitng list of donors. Or enter quit to exist current function")
		if user_input.lower() == "list":
			print(data.keys())

		elif user_input.lower() == "quit":
			break
		
		else:
			amount1 = int(input("how much would you like to donat?"))
			data[user_input.capitalize()] += [amount1]
			print("Thank you {} for your donation {}!".format(user_input.capitalize(), amount1))
			return data



#Creat a report function
def report(data):
	report_list = list()
	for x in data.keys():
		donation_sum = sum(data[x])
		donation_num = len(data[x])
		donation_average = donation_sum/donation_num
		report_list.append((x, donation_sum, donation_num, donation_average))
	
	def custom_sorting(tuple):
		return tuple[1]

	report_list.sort(key = custom_sorting, reverse = True)

	string_title = "{:<12}{} {:<12}{} {:<12}{} {:<12}".format("Donor Name","|","Total Given","|","Num Gifts","|","Average Gift")
	print(string_title)
	print("-"*len(string_title))

	for x in report_list:
		print("{:<12} ${:>12,.2f}  {:>12} ${:>12,.2f}".format(*x))

def all_letter(data):
    """Try to use a dict and the .format() method to produce the letter as one big template, the write into a txt file named with donor's name"""
    for name in data.keys():
        with open(name,"w") as f:
            f.write("Dear {},\n  Thank you for your very kind donation of {}.\n\
            It will be put to very good use.\n\
                               Sincerely,\n\
                               - The Team".format(name,sum(data[name])))


if __name__ == "__main__":
    while True:
        user_input = int(input("1. send a thank you to a donor\n2. report\n3. send letter to all\n4. quit"))
        if user_input == 4:
            break
        dct_opt = {1:thank_you, 2:report, 3:all_letter}
        dct_opt.get(user_input)(data)

