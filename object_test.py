"""
This the test module for the other modules.
This is where the working demo should be shown

Push the modules to the limit, extreme cases and make them work.
"""


import object_file_loader
import objcet_database


# print('hello')
# test01 = object_file_loader.FileLoader()
# print(test01.email, test01.fullname, test01.first, test01.ID, test01.last, test01.MAC)
#
# test01.set_file_name()
# test01.set_file_path()
# test01.file_loader()

test02 = objcet_database.LocalDatabase()
# test02.basic_info_table()
# test02.info_table()
# test02.visitor_log_table()
# test02.test_data_entry()
test02.test_data_read()
test02.test_data_delete()
test02.test_data_read()

