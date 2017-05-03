"""
This object will define the structure for basic employee information

Below is the description for each elements:
ID: unique four digits identification number of each individual, integer 
first: first name, string
last: last name, string
phone_number: cellphone number for SMS reminder feature, integer
MAC: MAC address for each individual's working computer, string
fullname: full name for display feature, string
email: email address for email reminder feature, string

*...
"""


class EmployeeBasicInfo:

    def __init__(self):
        self.ID = []
        self.first = []
        self.last = []
        self.phone_number = []
        self.MAC = []
        self.time = []

    @property
    def email(self):
        return '{}.{}@edag.se'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

