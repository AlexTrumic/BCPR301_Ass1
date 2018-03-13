from Cleaner import *;
import datetime;

class Validator():
    def Validate_Age(self, Given_Age):
        myCleaner = Cleaner()
        result = myCleaner.Clean_Age(Given_Age)
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

    def Validate_Birthday(self, Given_Birthday, Given_Age):
        output = False
        error = ""
        my_Cleaner = Cleaner()
        result = my_Cleaner.Clean_Birthday(Given_Birthday)
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

