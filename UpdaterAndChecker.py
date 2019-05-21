#Updater and Checker

import xlrd
import Employees
import Classes
import Store
import os.path

def main():

	
	#Tell the user how to exit program
	print("To Exit program enter 'exit'")
	
	#loop until done
	flag = True
	while flag:
		#get the user input
		print()
		#Ask user what is the name of the file
		print("What is the name of the file?")
		user_input = input()
		file_name = user_input+".xlsm"
		print(user_input)
		#check if the user wants to exit
		if user_input == 'exit':
			#if so then exit
			return	
		
		elif os.path.isfile(file_name):
			flag = False
			
		#if not a number tell the user
		else: 
			print("That's not a name of a file!")	
	
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
	try:
		wb = xlrd.open_workbook(file_name) 
		print("Selecting sheet")
	
	except:
		print("Ooops!")
		return
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
				for k in range(Employees.NUM_SECTIONS):
					#print(schedule.cell_value(i+2, k+2),end='')
					
					#loop through each section
					for m in range(len(Store.store_ct457.get_sections())):
					
						#if the store number is the same as the cell
						if Store.store_ct457.get_sections()[m].get_number() == schedule.cell_value(i+2, k+2):
						
							#add that section to a list
							some_sections.append(Store.store_ct457.get_sections()[m])
							break
							
				#Check if all section inputs are correct
				if len(some_sections) != Employees.NUM_SECTIONS:
					print("ERROR:",Employees.NUM_SECTIONS - len(some_sections)," invalid input(s) for a section for", working_today[i].get_name())	
					
				#add the list to the employee
				working_today[i].set_sections(some_sections)
				
				#working_today[i].print_employee()
				break
				
		#Check if all employee name inputs are correct
		if working_today[i] == None :
			print("ERROR: Employee",i+1,"in the list of employees names is not correct.")
	
	print("data retrieved")
	
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
			Store.store_ct457.aisle_responsibility (aisle, working_today)
			
		#if not an aisle tell the user
		except ValueError:
			print("That's not an aisle number!")
main()