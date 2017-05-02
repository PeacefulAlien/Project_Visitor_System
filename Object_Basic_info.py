"""
This object will define the basic employee information
ID: unique four digits identification number of each individual, integer 
first: first name, string
last: last name, string
phone_number: cellphone number for SMS reminder feature, integer
MAC: MAC address for each individual's working computer, string
fullname: full name for display feature, string
email: email address for email reminder feature, string
path: where is the list of employee information
*...
"""


import csv
import datetime


class employee():

	def __init__(self):
		self.ID = []
		self.first = []
		self.last = []
		self.phone_number = []
		self.MAC = []
		self.path = []
		self.time = []
	
	@property
	def email(self):
		return '{}.{}@edag.se'.format(self.first, self.last)
	
	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
		
	def set_path(self):
		result = 'n'
		while result != 'y':
			self.path = input('Please enter the full address for the initial file --> ')
			print('{}\nis this the right address for the input file? y/n'.format(self.path))
			result = input()
			if result == 'y':
				break
	
	
	def file_loader(self):
		pass