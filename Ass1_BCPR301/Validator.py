from Cleaner import *;
import datetime;

class Validator():

    #Ryan Parker
    def val_empid(self, employees, data):
        if len(data) == 4:
            if data[0].isalpha():
                pass
            else:
                error = 'frist charater must be alhpabetical'
                return False, error
            for x in data[1]:
                if x.isdigit():
                    pass
                else:
                    error = 'last 3 charaters in empid must be numbers'
                    return False, error
            for emp in employees:
                if emp.my_empid != data:
                    pass
                else:
                    error = 'empid exists'
                    return False, error
            error = ''
            return True, error
        else:
            error = 'empid must be four characters long'
            return False, error

    # Ryan Parker
    def val_gender(self, data):
        if data == "M" or data == "F":
            return True, ''
        else:
            error = 'gender must be: M or F'
            return False, error

    def Validate_Age(self, Given_Age):
        result = Given_Age
        error = ""
        output = False
        #Checks to see if the Cleaner could clean the Given_Age
        if(result[0] != None):
            current_Age = result[0]
            #Checks to see if current_Age is within the 0-99 range
            if 0 <= current_Age <= 99:
                output = True
            else:
                error = "Age not between 0 and 99"
        else:
            error = result[1]
        return output, error

    #Ryan Parker
    def val_bmi(self, data):
        if data == 'Normal' or data == 'Overweight' or data == 'Obesity' or data == 'Underweight':
            return True, ''
        else:
            error = 'bmi must be: Normal, Overweight, Obesity or Underweight'
            return False, error

    def Validate_Birthday(self, Given_Birthday, Given_Age):
        output = False
        error = ""
        result = Given_Birthday
        #Checks to see if the birthday was cleaned
        if(result[0] != None):
            if(result[1] == ""):
                date_Details = result[0].split("-")
                str_Day = date_Details[0]
                str_Month = date_Details[1]
                str_Year = date_Details[2]
                try:
                    given_Birth_Date = datetime.date(int(str_Year), int(str_Month), int(str_Day))
                    today = datetime.datetime.now()
                    should_Be_Age = today.year - given_Birth_Date.year - ((today.month, today.day) < (given_Birth_Date.month, given_Birth_Date.day))
                    if should_Be_Age == Given_Age:
                        output = True
                    else:
                        error = "The age given and birthday do not line up"
                except:
                    error = "Birthday is not a valid date"
            else:
                error = result[1]
        else:
            error = "Birthday wasnt not in a logical format"
        return output, error

