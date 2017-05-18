"""
This the test module for the other modules.
This is where the working demo should be shown

ALWAYS REMEMBER! THERE IS ONLY ONE RULE:
Push the modules to the limit, extreme cases and make them work.
"""


import object_input_file_loader
import objcet_database_main


test01 = object_input_file_loader.FileLoader()
# test01.set_file_name()
# test01.set_file_path()
# test01.file_name = 'test.csv'
# test01.file_path = 'C:\\Users\\sunzao\\Documents\\Python\\Project_Visitor_System'
test01.file_validation()
test01.file_loader()

test02 = objcet_database_main.DatabaseMain()
test02.info_table_drop()
