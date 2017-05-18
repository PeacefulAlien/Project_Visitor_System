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
        self.input_header_string = ''
        self.input_field_string = ''

    # functions regarding basic_info_table
    def basic_info_table_init(self, header):

        for i in range(0, len(header)):
            header[i] = ''.join(header[i].split())

        for i in range(0, len(header)-1):
            self.input_header_string += '{} TEXT, '.format(header[i])
            # self.input_header_string += header[i] + ' ' + 'TEXT,' + ' '
        self.input_header_string += '{} TEXT'.format(header[-1])
        # self.input_header_string += str(header[-1]) + ' ' + 'TEXT'

        self.cur.execute("""CREATE TABLE IF NOT EXISTS EmployeeBasicInfo
                        ({});""".format(self.input_header_string))

    def basic_info_table_drop(self):
        self.cur.execute("""DROP TABLE IF EXISTS EmployeeBasicInfo;""")
        self.conn.commit()

    def basic_info_table_reset(self):
        self.cur.execute("""DELETE FROM EmployeeBasicInfo;""")
        self.conn.commit()

    def basic_info_table_data_entry(self, field):

        for i in range(0, len(field)-1):
            self.input_field_string += '?, '
            # self.input_field_string += '?,' + ' '
        self.input_field_string += '?'

        self.cur.execute("""INSERT INTO EmployeeBasicInfo VALUES({});""".format(self.input_field_string), field)
        self.conn.commit()

    def basic_info_read(self):
        pass
    # functions regarding basic_info_table

    # functions regarding info_table
    def info_table_init(self, header):

        local_sql_string = '{}, {}'.format(header, self.input_header_string)

        self.cur.execute("""CREATE TABLE IF NOT EXISTS EmployeeInfo
                       ({});""".format(local_sql_string))

    def info_table_reset(self):
        self.cur.execute("""DELETE FROM EmployeeInfo;""")
        self.conn.commit()

    def info_table_drop(self):
        self.cur.execute("""DROP TABLE IF EXISTS EmployeeInfo;""")
        self.conn.commit()

    def info_table_data_entry(self, field):

        local_sql_string = ''
        for i in range(0, len(field)):
            local_sql_string += '?, '
        local_sql_string = '{}, {}'.format(local_sql_string, self.input_field_string)

        self.cur.execute("""INSERT INTO EmployeeInfo VALUES({});""".format(local_sql_string), field)
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
