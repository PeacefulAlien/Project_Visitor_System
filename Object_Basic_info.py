"""
This object will define the basic employee information and structure for the information
"""


import csv


class employee():

	def __init__(self, ID, first, last, phone_number):
		self.ID = []
		self.first = []
		self.last = []
		self.phone_number = []
	
	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
		
	@property
	def email(self):
		return '{}.{}@edag.se'.format(self.first.lower(), self.last.lower())
	
	def employee_basic_info_load(self):
		with open('employee_basic_info.csv') as input_file:
			
		
			employee_basic_info = csv.reader(input_file, delimiter=';')
			for row in employee_basic_info:
				self.ID.append(row)