#Program to retrieve schedule data

import xlrd
import Employees
import Classes
import Store
working_today = []
def main():

	
	#Tell the user how to exit program
	print("To Exit program enter 'exit'")
	
	#loop until done
	flag = True
	while flag:
		#get the user input
		print()
		#Ask user how many people are working today?
		print("How many employees are working sales today?")
		user_input = input()
		
		#check if the user wants to exit
		if user_input == 'exit':
			#if so then exit
			return	
		
		try:
			num_employees = int(user_input)
			flag = False
			
		#if not a number tell the user
		except ValueError:
			print("That's not an amount of people!")	
	
	print("Finding file")	
	# Give the location of the file 
	loc = ("May17-Sales.xlsm") 

	print("Opening file")
	# To open Workbook 
	wb = xlrd.open_workbook(loc) 
	print("Selecting sheet")
	#get the sheet of the schedule
	schedule = wb.sheet_by_index(3)
	
	print("Retreving data")
	#list of names of people working today
	names_working_today = [None] * num_employees
	working_today = [None] * num_employees
	
	
	#look through the number of employees working tod
	for i in range(num_employees):
	
		#set the names of the people working form the spreadsheet
		names_working_today[i] = schedule.cell_value(i+2, 0) 
		
		#loop through each employee in the store
		for j in range(len(Employees.employee_list)):
			
			#and check if they are on the list of people working today
			if names_working_today[i] == Employees.employee_list[j].get_name():
			
				#if they are working today add them to an object list
				working_today[i] = Employees.employee_list[j]
				some_sections = []
				#loop through each column
				for k in range(20):
					
					#loop through each section
					for m in range(len(Store.store_ct457.get_sections())):
					
						#if the store number is the same as the cell
						if Store.store_ct457.get_sections()[m].get_number() == schedule.cell_value(i+2, k+2):
						
							#add that section to a list
							some_sections.append(Store.store_ct457.get_sections()[m])
							break
							
				#add the list to the employee
				working_today[i].set_sections(some_sections)
				break
	
	print("data retrieved")

main()