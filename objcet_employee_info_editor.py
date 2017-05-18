"""
This object will define the structure for basic employee info,
manipulate the basic info to all the info needed for the application

Description:
ID: unique four digits identification number of each individual, integer 
first: first name, string
last: last name, string
phone_number: cellphone number for SMS reminder feature, integer
MAC: MAC address for each individual's working computer, string
fullname: full name for display feature, string
email: email address for email reminder feature, string

"""


class EmployeeInfoEditor:

    def __init__(self):
        self.first = []
        self.last = []
        self.ID = []
        self.phone_number = []
        self.MAC = []

    @property
    def email(self):
        return '{}.{}@edag.se'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)



