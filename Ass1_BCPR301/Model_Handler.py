from Reader import *
from Validator import *
from My_CMD import *
from employee_db import EmployeeDB
from Employee import Employee
from Cleaner import Cleaner

class Model_Handler():
    all_My_Employees = {}
    my_validator = Validator()
    my_reader = Reader()
    my_database = EmployeeDB()
    clean = Cleaner()
    user = ""
    error_File = ""
    database_Location = ""
    database_userName = ""
    database_password = ""

    def  __init__(self, config_File_Location):
        config_contents = self.my_reader.read_Config(config_File_Location);
        self.user = config_contents[0]
        self.error_File = config_contents[1]
        self.database_Location = config_contents[2]
        self.database_userName = config_contents[3]
        self.database_password = config_contents[4]

    def Get_All_Employees_Database(self):
        #Fill allMyEmployees with data from database
        con = self.my_database.connect()
        try:
            c = con.cursor()
            sql = "SELECT * FROM employees"
            c.execute(sql)
            for row in c:
                empid = row[0]
                gender = row[1]
                age = row[2]
                sales = row[3]
                bmi = row[4]
                salary = [5]
                birthday = [6]
                emp = Employee(empid, gender, age, sales, bmi, salary, birthday)
                self.all_My_Employees[empid] = emp
            con.close()
        except:
            print('faild to retrive employees from database')


    def Save_New_Employees_Database(self):
        #Database is updated with new all_My_Employees
        for emp in self.all_my_employees:
            empid = emp.my_empid
            gender = emp.my_gender
            age = emp.my_age
            sales = emp.my_sales
            bmi = emp.my_bmi
            salary = emp.my_salary
            birthday = emp.my_birthday
            self.d.save_employee(empid, gender, age, sales, bmi, salary, birthday)

    #Validation Handlers
    def Validate_Age(self, given_Age):
        return self.my_validator.Validate_Age(given_Age)

    def add_employee(self):
        val = self.my_validator
        c = self.clean

        empid = c.clean_empid(input("employee id number e.g. A102: "))
        while val.val_empid(empid) == False:
            print('invalid ID try again')
            empid = input("employee id number e.g. A102: ")

        gender = c.clean_gender(input("employee's gender M or F: "))
        while val.val_gender(gender) == False:
            print('invalid gender try again')
            gender = input("employee's gender M or F: ")

        age = c.Clean_Age(input("employee's age: "))
        while val.Validate_Age(age)[0] == False:
            print(val.Validate_Age(age)[1])
            age = input("employee's age: ")

        sales = input("number of sales employee has made (3 digit number): ")
        while val.val_sales(sales) == False:
            print('invalid sales try again: ')
            sales = input("number of sales employee has made (3 digit number): ")

        bmi = c.clean_bmi(input("employee's bmi (Normal, Overweight, Obesity, or Underweight): "))
        while val.val_bmi(bmi) == False:
            print('invalid bmi try again: ')
            bmi = input("employee's bmi (Normal, Overweight, Obesity, or Underweight): ")

        salary = input("employee's salary(5 digit number): ")
        while val.val_salary(salary) == False:
            print('invalid salary try again: ')
            salary = input("employee's salary(5 digit number): ")

        birthday = c.Clean_Birthday(input("employee's birthday DD-MM-YYYY: "))
        while val.Validate_Birthday(birthday, age) == False:
            print('invalid bithday try again: ')
            birthday = input("employee's birthday DD-MM-YYYY: ")
        emp = Employee(empid, gender, age, sales, bmi, salary, birthday)

        self.all_My_Employees[empid] = emp
