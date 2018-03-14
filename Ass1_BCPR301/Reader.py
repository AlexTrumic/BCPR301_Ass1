import xml.etree.ElementTree as ET
from Employee import Employee # Ryan: changed the star to employee dont know if it will break your code or not
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

    def read_file_txt(self,all_my_employees):
        with open("employees.txt", "r") as file:
            data = file.readlines
            for line in data:
                emp = line.split(",")
                employee = Employee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6])
                all_my_employees[emp[0]] = employee
        return all_my_employees


    def write_file_txt(self, employees):
        with open("employees.txt", "w") as file:
            for emp in employees:
                empid = emp.my_empid
                gender = emp.my_gender
                age = emp.my_age
                sales = emp.my_sales
                bmi = emp.my_bmi
                salary = emp.my_salary
                birthday = emp.my_birthday
                file += empid + "," + gender + "," + age + "," + sales + "," + bmi + "," + salary + "," + birthday + "/n"