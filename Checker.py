#Program to check who covers a specific aisle

#import the the different files
import Store	
import Employees

def main():

	#Tell the user how to exit program
	print("To Exit program enter 'exit'")
	
	#loop forever
	while True:
		#get the user input
		print()
		print("Enter what aisle you want to know who is responisble for.")
		user_input = input()
		
		#check if the user wants to exit
		if user_input == 'exit':
			#if so then exit
			break
			
		#if the input is an asile number then
		try:
			aisle = int(user_input)
			
			#check who is responsible for that aisle
			Store.store_ct457.aisle_responsibility (aisle, Employees.employee_list)
			
		#if not an aisle tell the user
		except ValueError:
			print("That's not an aisle number!")		
	
main()