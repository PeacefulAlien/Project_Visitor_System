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
		self.first_name = []
		self.last_name = []
		self.full_name = []
		self.email = []
		self.ID = []
		self.mobilephone = []
		
		self.itemdex = []
		self.aviliable_list = []
	
	def read_data(self):
		with open('employee_inlist.csv') as csvfile:
			employee_inlist = csv.reader(csvfile, delimiter=';')
			for row in employee_inlist:
				self.first_name.append(row[0])
				self.last_name.append(row[1])
				self.full_name.append(row[0] + ' ' + row[1])
				self.ID.append(row[2])
				self.mobilephone.append(row[3])
		return self.first_name, self.last_name, self.full_name, self.ID, self.mobilephone
	
	def find_employee(self):
		while True:
			item = input("Please enter the information you have: ")
			""" Request for an input of the information, potential interface """
			if item in self.first_name:
				self.itemdex.append(self.first_name.index(item))
				break
			elif item in self.last_name:
				self.itemdex.append(self.last_name.index(item))
				break
			elif item in self.full_name:
				self.itemdex.append(self.full_name.index(item))
				break
			elif item in self.ID:
				self.itemdex.append(self.ID.index(item))
				break
			elif item in self.mobilephone:
				self.itemdex.append(self.mobilephone.index(item))
				break
			else:
				print("Information Imcomplete!!!\n")
		return self.itemdex
	
	def demo_employee(self):
		print("The employee you are looking for is listed below:")
		for index in self.itemdex:
			print("{}".format(self.full_name[index]))
	
	def checkin_func(self):
		pass
	
	def checkout_func(self):
		pass

		
"""
	below is the testing cases
"""		
if __name__ == '__main__':
	for i in range(5):
		employee_test = employee()
		employee_test.read_data()
		employee_test.find_employee()
		employee_test.demo_employee()
	