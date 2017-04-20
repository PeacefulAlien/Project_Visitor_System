"""
This object will define the basic employee information
ID: unique four digits identification number of each individual, integer 
first: first name, string
last: last name, string
phone_number: cellphone number for SMS reminder feature, integer
MAC: MAC address for each individual's working computer, string
fullname: full name for display feature, string
email: email address for email reminder feature, string
*...
"""


import csv


class employee():

	def __init__(self, ID, first, last, phone_number, MAC):
		self.ID = []
		self.first = []
		self.last = []
		self.phone_number = []
		self.MAC = []
		
	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
		
	@property
	def email(self):
		return '{}.{}@edag.se'.format(self.first.lower(), self.last.lower())
	
	def employee_basic_info_load(self):
		with open('employee_basic_info.csv') as input_file:
			if csv.Sniff.has_header(input_file):
				
		
			employee_basic_info = csv.reader(input_file, delimiter=';')
			for row in employee_basic_info:
				self.ID.append(row)