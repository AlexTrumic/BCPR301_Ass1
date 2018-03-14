import sqlite3

class EmployeeDB:

    def connect(self):
        try:
            con = sqlite3.connect('employees.db')
            return con
        except:
            print('connection to database failed')

    def create_table(self):
        con = self.connect()
        try:
            c = con.cursor()
            sql = """
            CREATE TABLE employees (
            empid TEXT(4) PRIMARY KEY UNIQUE,
            gender CHAR(1),
            age INTERGER,
            sales INTEGER,
            bmi VARCHAR(10),
            salary INTEGER,
            birthday TEXT);"""
            c.execute(sql)
            con.commit()
            con.close()
        except:
            print('table aready exists')

    def save_employee(self, empid, gender, age, sales, bmi, salary, birthday):
        con = self.connect()
        try:
            c = con.cursor()
            insert = "INSERT INTO employees(empid, gender, age, sales, bmi, salary, birthday) "
            values = "VALUES('" + empid + "', '" + gender + "', " + age + ", " + sales + ", '" + bmi + "', " + salary + ", '" + birthday + "');"
            sql = insert + values
            c.execute(sql)
            con.commit()
            con.close()
        except:
            print('failed to add employee')

    def update_employee(self, empid, what, data):
        con = self.connect()
        try:
            c = con.cursor()
            update = 'UPDATE employees'
            set = "SET " + what + "=" + data
            where = "WHERE empid = " + empid
            sql = update + set + where
            c.execute(sql)
            con.close()
        except:
            print('failed to update employee')


