from models.admin import Admin
from models.employee import Employee
from models.manager import Manager
from models.message import Message

import mysql.connector
from mysql.connector import Error


# This controller will be responsible to create/alter/delete models and access database
class Controller:
    def __init__(self):
        self.active_users = []

    def retrieve_user_info(self, employee_no):
        return 0
        # try:
        #     connection = mysql.connector.connect(host='localhost',
        #                                          database='Electronics',
        #                                          user='pynative',
        #                                          password='pynative@#29')
        #     if connection.is_connected():
        #         db_info = connection.get_server_info()
        #         print("Connected to MySQL Server version ", db_info)
        #         cursor = connection.cursor()
        #         # perform SQL query
        #         cursor.execute("select database();")
        #         record = cursor.fetchone()
        #         print("You're connected to database: ", record)
        #
        # except Error as e:
        #     print("Error while connecting to MySQL", e)
        # finally:
        #     if connection.is_connected():
        #         cursor.close()
        #         connection.close()
        #         print("MySQL connection is closed")
        # # should return an object
        # return 0

    def authenticate_user(self, employee_no, password, user_type):
        return False

    def initialize_user(self, user):
        self.active_users.append(user)

    def process_login(self, employee_no, password, user_type):
        # once user successfully authenticate
        if self.authenticate_user(employee_no, password, user_type):
            user_obj = self.retrieve_user_info(employee_no)
            if type == 'employee':
                employee = Employee()
            elif type == 'manager':
                manager = Manager()
            else:
                admin = Admin()
            self.initialize_user()
