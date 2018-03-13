from Reader import *
from Validator import *
from My_CMD import *


class Model_Handler():
    all_My_Employees = {}
    my_Validator = Validator()
    my_Reader = Reader()
    user = ""
    error_File = ""
    database_Location = ""
    database_userName = ""
    database_password = ""

    def  __init__(self, config_File_Location):
        config_contents = self.my_Reader.read_Config(config_File_Location);
        self.user = config_contents[0]
        self.error_File = config_contents[1]
        self.database_Location = config_contents[2]
        self.database_userName = config_contents[3]
        self.database_password = config_contents[4]

    def Get_All_Employees_Database(self):
        #Fill allMyEmployees with data from database
        pass

    def Save_New_Employees_Database(self):
        #Database is updated with new all_My_Employees
        pass

    #Validation Handlers
    def Validate_Age(self, given_Age):
        return self.my_Validator.Validate_Age(given_Age)

