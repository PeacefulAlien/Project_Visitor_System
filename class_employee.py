"""
	Another approach to implement one of the stories of the project
	the class_employee basically read the employee_inlist.csv file
	as input and generate datebase for the future usage
	
	Method descriptions:
	read_data(): load the employee_inlist.csv file
	find_employee(): find the desired employee in the database
	checkin_func(): employee check in at the office
	checkout_func(): employee check out from the office
	
"""


import csv

class employee:

	def __init__(self):
		self.first_name = None
		self.last_name = None
		self.full_name = None
		self.email = None
		self.ID = None
		self.mobilephone = None
		self.aviliable_list = None
	
	def read_data():
		with open('employee_inlist.csv') as csvfile:
			employee_inlist = csv.reader(csvfile, delimiter=';')
			for row in employee_inlist:
				self.first_name.append(row[0])
				self.last_name.append(row[1])
				self.full_name.append(row[0] + ' ' + row[1])
				self.ID.append(row[2])
				self.mobilephone.append(row[3])
		return self.first_name, self.last_name, self.full_name, self.ID, self.mobilephone
	
	def find_employee(item):
		item = input("Please enter the information you have: ")
		""" Request for an input of the information, potential interface """
		itemdex = None
		if item in self.first_name:
			itemdex.append(self.first_name.index(item))
		elif item in self.last_name:
			itemdex.append(self.last_name.index(item))
		elif item in self.full_name:
			itemdex.append(self.full_name.index(item))
		elif item in self.ID:
			itemdex.append(self.ID.index(item))
		elif item in self.mobilephone:
			itemdex.append(self.mobilephone.index(item))
		else:
			itemdex.append("Invalid input")
		return itemdex
		
	def checkin_func():
		pass
	
	def checkout_func():
		pass
	 