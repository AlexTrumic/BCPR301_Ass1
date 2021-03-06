from cmd import Cmd
from Model_Handler import *
import tkinter as tk
from tkinter import filedialog


class My_CMD(Cmd):

    def __init__(self, model_Handler):
        Cmd.__init__(self)
        self.My_Model_Handler = model_Handler
        self.My_Model_Handler.Get_All_Employees_Database()
        self.prompt = ">>> "
        self.intro = "Welcome to BCPR301_Ass1 Interpreter \nIf help with options is needed type 'help'"

    def do_ImportFile(self, file_type):
       """
        Syntax: ImPortFile(file_type)
        Adds all new employees from file to Model_Handler.All_My_Employees
        param: file_type : a string representing what type of file it is. Options: txt, xml, csv
        returns: None
       """
       root = tk.Tk()
       root.withdraw()
       file_path = filedialog.askopenfilename()
       my_Reader = Reader()

       if(file_type == "txt"):
           pass

       if (file_type == "xml"):
           self.My_Model_Handler.all_My_Employees.update(my_Reader.XML_Reader(file_path, self.My_Model_Handler.error_File))

       if (file_type == "csv"):
           pass


    def do_SaveNewEmployees(self, line):
        """
        Syntax: SaveNewEmployees
        Saves all newly Added Employees to database
        Prints 'Database updated' if successful or errors if not
        returns: none
        """
        self.My_Model_Handler.Save_New_Employees_Database()
        print("Database updated")

    def do_InputEmployee(self, line):
        """
        syntax: InputEmployee()
        Asks user for inputs for a new Employee
        Adds new single employee to all_My_Employees
        returns: none
        """
        self.My_Model_Handler.add_employee()


        #Then adds employee to All_My_Employees()

    def do_Graph(self, typeGraph):
        """
        syntax: Graph(self, typeGraph, value1, value2)
        Displays a graph with the two values given or the error as to why it can not be displayed
        param: typeGraph : A string with the type of graph wanted eg: Bar, Pie, Line
        returns: none
        """

        # If typeGraph == bar
        #createBarGraph

        # If typeGraph == line
        # createLineGraph

        # If typeGraph == pie
        # createPieGraph

        # If values cannot be represented in graph print why they cannot

    def do_quit(self, line):
        """
        Quit from MyCMD
        return: True
        """
        want_save = input("Do you wish to save new Employees to Database? Y/N")
        while(want_save not in ["y", "Y", "n", "N"]):
            want_save = input("Do you wish to save new Employees to Database? Y/N")
        if(want_save in ["y","Y"]):
            self.My_Model_Handler.Save_New_Employees_Database();
            print("Database Updated")
        print("Quitting ......")
        return True
