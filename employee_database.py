"""
This object file is for building the backend
database for the application using SQlite
"""


import sqlite3


conn = sqlite3.connect('employee_info.db')
c = conn.cursor()


def creat_table():
    c.execute("CREATE TABLE IF NOT EXISTS EmployeeInfo(first TEXT, last TEXT, ID TEXT, phone_number TEXT, availability REAL)")


def data_entry():
    c.execute("INSERT INTO EmployeeInfo VALUES('agent', 'yolo', '2007', '0760002007', 1)")
    conn.commit()
    c.close()
    conn.close()

creat_table()
data_entry()
