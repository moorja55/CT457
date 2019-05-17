#Employee class holds essential information of an employee
class Employee:

	#Each employee has their employee number, name and section
	def __init__(self, employee_number, name, section):
		self.__employee_number = employee_number
		self.__name = name
		self.__section = section
		
	def get_employee_number(self):
		return self.__employee_number
	
	def get_name(self):
		return self.__name
		
	def get_section(self):
		return self.__section
		
	def set_section(self, section):
		self.__section = section
		
	#display the employee
	def print_employee (self):
		print('Number: ',self.__employee_number())
		print('Name: ',self.__get_name())
		print('Section: ', self.__section().get_name())

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
		
		#loop through each section
		for  i in range(len(self.__sections)):
			#loop through each aisle
			for  k in range(len(self.__sections[i].get_aisles())):
				#if it is the correct aisle
				if self.__sections[i].get_aisles()[k] == aisle:
					#then check what employee has that section
					for m in range(len(employees)):
						#if the employee has that section then
						if employees[m].get_section().get_name() == self.__sections[i].get_name():
							#display that they have that aisle and increase the counter
							print(n,".",employees[m].get_name()," is in section ",self.__sections[i].get_name(),sep='')
							n = (n + 1)
	
#Section is an area of the store a sales assosciate is responsible for
class Section:

	
	#Each section has a name and what aisles are in that section	
	def __init__(self, name, ailes):
		self.__name = name
		self.__ailes = ailes
		
	def get_name(self):
		return self.__name
		
	def get_aisles(self):
		return self.__ailes
	
		
	