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


class DatabaseMain:

    def __init__(self):
        self.conn = sqlite3.connect('database_main.db')
        self.cur = self.conn.cursor()

    # functions regarding basic_info_table
    def basic_info_table_init(self, header):

        for i in range(0, len(header)):
            header[i] = ''.join(header[i].split())

        sql_string_01 = ''
        for i in range(0, len(header)-1):
            sql_string_01 += str(header[i]) + ' ' + 'TEXT,' + ' '
        sql_string_01 += str(header[-1]) + ' ' + 'TEXT'

        self.cur.execute("""CREATE TABLE IF NOT EXISTS EmployeeBasicInfo
                        ({});""".format(sql_string_01))

    def basic_info_table_drop(self):
        self.cur.execute("""DROP TABLE IF EXISTS EmployeeBasicInfo;""")
        self.conn.commit()

    def basic_info_table_reset(self):
        self.cur.execute("""DELETE FROM EmployeeBasicInfo;""")
        self.conn.commit()

    def basic_info_table_data_entry(self, field):

        sql_string_02 = ''
        for i in range(0, len(field)-1):
            sql_string_02 += '?,' + ' '
        sql_string_02 += '?'

        self.cur.execute("""INSERT INTO EmployeeBasicInfo VALUES({});""".format(sql_string_02), field)
        self.conn.commit()
    # functions regarding basic_info_table

    # functions regarding info_table
    def info_table_init(self):

        sql_string_03 = ''

        self.cur.execute("""CREATE TABLE IF NOT EXISTS EmployeeInfo
                       ({});""".format(sql_string_03))

    def info_table_reset(self):
        self.cur.execute("""DELETE FROM EmployeeInfo;""")
        self.conn.commit()

    def info_table_data_entry(self, field):
        self.cur.execute("""INSERT INTO EmployeeInfo VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", field)
        self.conn.commit()
    # functions regarding info_table

    # functions regarding testing
    def test_data_entry(self):
        self.cur.execute("""INSERT INTO EmployeeInfo VALUES
                        ('Zao', 'yolo', 'agent yolo', '2007', '0760002007', 'XXXXXXXX', 'agent.yolo@edag.com', '0');""")
        self.cur.execute("""INSERT INTO EmployeeBasicInfo VALUES
                        ('Zao', 'Sun', '2070', '0763929606', 'XXXXXXX');""")
        self.conn.commit()

    def test_data_read(self):
        self.cur.execute("""SELECT * FROM EmployeeInfo;""")
        for row in self.cur.fetchall():
            print('{}'.format(row))
        self.cur.execute("""SELECT * FROM EmployeeBasicInfo;""")
        for row in self.cur.fetchall():
            print('{}'.format(row))
    # functions regarding testing
