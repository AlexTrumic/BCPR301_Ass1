from employee import Employee
class EmployeeHandeler:

    all_my_employees = []

    def add_employee(self, empid, gender, age, sales, bmi, salary, birthday):
        employee = Employee(empid, gender, age, sales, bmi, salary, birthday)
        self.all_my_employees.append(employee)

    def update_employe(self, empid, new_gender, new_age, new_sales, new_bmi, new_salary, new_birthday):
        employee = self.find_employee(self, empid)
        employee.my_gender = new_gender
        employee.age = new_age
        employee.sales = new_sales
        employee.my_bmi = new_bmi
        employee.my_salary = new_salary
        employee.my_birthday = new_birthday

    def delete_employee(self, empid):
        employee = self.find_employee(self, empid)
        del employee

    def sort_employees(self):
        pass

    def find_employee(self, empid):
        for employee in self.all_my_employees:
            if employee(empid) == empid:
                return employee
