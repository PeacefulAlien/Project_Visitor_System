"""
This object will serve the function to build a local database
together with the application, so the employee information can be
used in the application multiple times without using the memory all
the time.
Once it is built, this object can serve the function to interact with
the database.

Tables:
EmployeeInfo: contains all the information the application needs
EmployeeBasicInfo: the raw information pulled from input csv file
VisitorLog: a log where the record of visitors is kept for further usage

Methods:
test_xxxx: these methods are just for testing the database
"""


import sqlite3
import objcet_employee_basic_info


class LocalDatabase(objcet_employee_basic_info.EmployeeBasicInfo):

    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('employee_info.db')
        self.c = self.conn.cursor()

    def info_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS EmployeeInfo
                       (first TEXT,
                       last TEXT,
                       full_name TEXT,
                       ID TEXT,
                       phone_number TEXT,
                       MAC TEXT,
                       email TEXT,
                       availability INTEGER)""")

    def basic_info_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS EmployeeBasicInfo
                        (first TEXT,
                        last TEXT,
                        ID TEXT,
                        phone_number TEXT,
                        MAC TEXT)""")

    def visitor_log_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS VisitorLog
                        (name TEXT,
                        date TEXT,
                        time TEXT,
                        relevant_personnel TEXT)""")

    def test_data_entry(self):
        self.c.execute("""INSERT INTO EmployeeInfo VALUES
                        ('Zao', 'yolo', 'agent yolo', '2007', '0760002007', 'XXXXXXXX', 'agent.yolo@edag.com', '0')""")
        self.c.execute("""INSERT INTO EmployeeBasicInfo VALUES
                        ('Zao', 'Sun', '2070', '0763929606', 'XXXXXXX')""")
        self.c.execute("""INSERT INTO VisitorLog VALUES
                        ('Jacob Pihl', '2017-01-01', '09:20:22', 'Zao Sun')""")
        self.conn.commit()
        # self.c.close()
        # self.conn.close()

    def test_data_delete(self):
        self.c.execute("""DELETE FROM EmployeeInfo""")
        self.c.execute("""DELETE FROM EmployeeBasicInfo""")
        self.c.execute("""DELETE FROM VisitorLog""")

    def test_data_read(self):
        self.c.execute("""SELECT * FROM EmployeeInfo""")
        for row in self.c.fetchall():
            print('{}'.format(row))
        self.c.execute("""SELECT * FROM EmployeeBasicInfo""")
        for row in self.c.fetchall():
            print('{}'.format(row))
        self.c.execute("""SELECT * FROM VisitorLog""")
        for row in self.c.fetchall():
            print('{}'.format(row))

    def dynamic_data_entry(self):
        pass

