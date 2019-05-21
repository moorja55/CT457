#to check the time for what section to look at
from datetime import datetime
#to randomly genearate time for testing
import random

#Employee class holds essential information of an employee
class Employee:

	#Each employee has their employee number, name and section
	def __init__(self, employee_number, name, sections):
		self.__employee_number = employee_number
		self.__name = name
		self.__sections = sections
	def get_employee_number(self):
		return self.__employee_number
	
	def get_name(self):
		return self.__name
		
	def get_sections(self):
		return self.__sections
		
	def get_section(self,num):
		return self.__sections[num]
		
	def set_employee_number(self,num):
		self.__employee_number = num
		
	def set_sections(self, sections):
		self.__sections = sections
		
	#display the employee
	def print_employee (self):
		print('Number: ',self.__employee_number,'Name: ',self.__name)
		for i in range(len(self.__sections)):
			print(self.__sections[i].get_number(),end='')
		print()

#Store is currently just a list of sections
#But it seems like it should be an object		
class Store:
	
	def __init__(self, name, sections):
		self.__name = name
		self.__sections = sections
		
	def get_name (self):
		return self.__name
	def get_sections(self):
		return self.__sections
		
	#check who is responsible for an aisle
	def aisle_responsibility (self, aisle, employees):
		#number of employees responsible for the aisle
		n= 1
		
		#get what time it is
		hour = datetime.now().hour
		minute = datetime.now().minute
		
		#Test random times
		#hour = random.randint(0,24)
		#minute = random.randint(0,60)
		
		#and format time into an index
		#print('time = (',hour,' - 7) * 2')
		time = (hour - 7) * 2
		if minute > 29:
			time += 1;
		
		#print(hour,":", minute,"=",time)	
		
		if time >= 32 or time < 0:
			print("No one working now")
			return
			
		#loop through each section
		for  i in range(len(self.__sections)):
			#loop through each aisle
			for  j in range(len(self.__sections[i].get_aisles())):
				
				#check if aisle is in that section
				if self.__sections[i].get_aisles()[j][0] <= aisle and aisle <= self.__sections[i].get_aisles()[j][1]:
					
					#then check what employee has that section
					for k in range(len(employees)):
					
						#employees[k].print_employee()
						
						#if the employee has that section then
						if employees[k].get_section(time).get_number() == self.__sections[i].get_number():
						
							#display that they have that aisle and increase the counter
							print(n,".",employees[k].get_name()," is in section ",self.__sections[i].get_name(),sep='')
							n = (n + 1)
	
#Section is an area of the store a sales assosciate is responsible for
class Section:
	
	#Each section has a name and what aisles are in that section	
	def __init__(self, number, name, ailes):
		self.__number = number
		self.__name = name
		self.__ailes = ailes

	def get_number(self):
		return self.__number
	
	def get_name(self):
		return self.__name
		
	def get_aisles(self):
		return self.__ailes
		
	def get_number(self):
		return self.__number