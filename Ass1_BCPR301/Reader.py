import xml.etree.ElementTree as ET
from Employee import *
from Validator import *

class Reader():

    def XML_Reader(self, file_Location, error_File_Location):
        MyValidator = Validator()
        my_Employees = {}
        tree = ET.parse(file_Location)
        root = tree.getroot()
        for user in root.findall('user'):
            # Need to Validate all given data
            empid = user.get('EMPID')
            gender = user.find('gender').text
            age = MyValidator.Validate_Age(user.find('age').text)
            sales = user.find('sales').text
            bmi = user.find('BMI').text
            salary = user.find('salary').text
            birthday = MyValidator.Validate_Birthday(user.find('birthday').text, age)
            #For each item in new Employee need to check that they have a value after being vlaidated

            #new_Employee = Employee(empid, gender, int(age), int(sales), bmi, int(salary), birthday)
            #my_Employees[new_Employee.EMPID] = new_Employee
        return my_Employees

    def read_Config(self, file_Location):
        tree = ET.parse(file_Location)
        root = tree.getroot()
        config_user = root.findall('user')[0].text
        config_error_file = root.findall('errorFile')[0].text
        for database in root.findall('database'):
            config_ddb_location = database.find('location').text
            config_ddb_username = database.find('username').text
            config_ddb_password = database.find('password').text
        return config_user,config_error_file, config_ddb_location, config_ddb_username, config_ddb_password