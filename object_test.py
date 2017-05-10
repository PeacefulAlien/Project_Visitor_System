"""
This the test module for the other modules.
This is where the working demo should be shown

Push the modules to the limit, extreme cases and make them work.
"""

import objcet_employee_basic_info
import object_file_loader

# test01 = objcet_employee_basic_info.EmployeeBasicInfo()
# print("First:{}\n"
#       "Last:{}\n"
#       "Fullname:{}\n"
#       "Email:{}\n"
#       "ID:{}\n"
#       "Phonenumber:{}\n"
#       "MAC:{}\n"
#       .format(test01.first,
#               test01.last,
#               test01.fullname,
#               test01.email,
#               test01.ID,
#               test01.phone_number,
#               test01.MAC))
#
# test02 = object_file_loader.FileLoader()
# print("Default Path:{}\n".format(test02.path))
# test02.set_path()
# print("New Path:{}\n".format(test02.path))
#
# test03 = object_file_loader.FileLoader()
# test03.path = 'sunzao'
# test03.set_path()
# print("New Path:{}\n".format(test03.path))

test04 = object_file_loader.FileLoader()
# test04.set_path()
# print(type(test04.path))
#test04.set_size()
test04.file_loader()
