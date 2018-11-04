#hw3, mailroom

data = {"Tom":[100,200], "Tim":[3000], "Ken": [888,888,888], "Ted":[8000,5000,500], "Jon":[1000,6000]}

#Send a thank you function 
def thank_you(data):
	while True:
		user_input = input("please enter the name of donor. You can enter list to see the exisitng list of donors. Or enter quit to exist current function")
		if user_input.lower() == "list":
			print(data.keys())

		if user_input.lower() == "quit":
			break
		
		elif user_input.capitalize() in list(data.keys()):
			amount1 = int(input("how much would you like to donat?"))
			data[user_input.capitalize()].append(amount1)
			print("Thank you {} for your donation {}!".format(user_input.capitalize(), amount1))
			return data
			break
			
		else:
			amount2 = int(input("how much would you like to donat?"))
			data[user_input.capitalize()] = list()
			data[user_input.capitalize()].append(amount2)
			print("Thank you {} for your donation {}!".format(user_input.capitalize(), amount2))
			return data
			break


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




if __name__ == "__main__":
	while True:
		user_input = int(input("You have 3 options to choose 1. send a thank you, 2. report, 3 exit. please pick the option by the number 1,2,3"))
		if user_input == 1:
			thank_you(data)
		elif user_input == 2:
			report(data)
		elif user_input == 3:
			break
		else:
			pass
