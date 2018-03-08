from cmd import Cmd
from employee_handler import EmployeeHandeler
from Validator import Validator

class Quitter(Cmd):
    """
    single command processor example
    """
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.my_name = "unknown"
        self.emp_handeler = EmployeeHandeler()
        self.val = Validator()

    def do_name(self, the_name):
        if the_name:
            self.my_name = the_name
        print(self.my_name)

    def do_addemployee(self, line):
        """

        Syntax: addemployee
        Starts the add employee process
        :pram: none
        :return: none
        """
        val = self.val

        empid = input("employee id number e.g. A102: ")
        while val.val_empid(empid) == False:
            if val.val_empid(empid):
                pass
            else:
                print('invalid ID try again')
                empid = input("employee id number e.g. A102: ")

        gender = input("employee's gender M or F: ")
        while val.val_gender(gender) == False:
            if val.val_gender(gender):
                pass
            else:
                print('invalid gender try again')
                gender = input("employee's gender M or F: ")

        age = input("employee's age: ")
        while val.val_age(age) == False:
            if val.val_age(age):
                pass
            else:
                print('invalid age try again')
                age = input("employee's age: ")

        sales = input("number of sales employee has made (3 digit number): ")
        while val.val_sales(sales) == False:
            if val.val_sales(sales):
                pass
            else:
                print('invalid sales try again: ')
                sales = input("number of sales employee has made (3 digit number): ")

        bmi = input("employee's bmi (Normal, Overweight, Obesity, or Underweight): ")
        while val.val_bmi(bmi) == False:
            if val.val_bmi(bmi):
                pass
            else:
                print('invalid bmi try again: ')
                bmi = input("employee's bmi (Normal, Overweight, Obesity, or Underweight): ")

        salary = input("employee's salary(5 digit number): ")
        while val.val_salary(salary) == False:
            if val.val_salary(salary):
                pass
            else:
                print('invalid salary try again: ')
                salary = input("employee's salary(5 digit number): ")

        birthday = input("employee's birthday DD-MM-YYYY: ")
        while val.val_birthday(birthday) == False:
            if val.val_birthday(birthday):
                pass
            else:
                print('invalid bithday try again: ')
                birthday = input("employee's birthday DD-MM-YYYY: ")

        self.emp_handeler.add_employee(empid, gender, age, sales, bmi, salary, birthday)

    def do_greet(self, the_name):
        """
        Syntax: greet [the_name]
        Greet the named person
        :param the_name: a string representing a person's name
        :return: None
        """
        if the_name:
            print("Hello " + the_name)
        else:
            print("Hello " + self.my_name)

    def do_quit(self, line):
        print("Quitting ......")
        return True

    def help_quit(self):
        print("\n".join(['Quit from my CMD', ':return: True']))

    do_q = do_quit

if __name__ == "__main__":
    quitter = Quitter()
    quitter.cmdloop()
