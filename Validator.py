from Cleaner import Cleaner

class Validator(object):

    clean = Cleaner()

    def val_empid(self, data):
        data = self.clean.clean_empid(data)
        if len(data) == 4:
            if data[0].isalpha():
                pass
            for x in data[1]:
                if x.isdigit():
                    pass
                else:
                    return False
            return True
        else:
            return False

    def val_gender(self, data):
        data = self.clean.clean_gender(data)
        if data == "M"or data == "F":
            return True
        else:
            return False

    def val_age(self, data):
        self.clean.clean_age(data)
        return True

        def Validate_Sales(self, Given_Sales):
        #check if the sales within range
        pattern = re.compile(r'\d{3}')
        if pattern.match(Given_Sales):
            return True
        else:
            ValueError as e
            return Given_Sales, e

    def val_bmi(self, data):
        data = self.clean.clean_bmi(data)
        if data == 'Normal' or data == 'Overweight' or data == 'Obesity' or data == 'Underweight':
            return True
        else:
            return False

    def Validate_Salary(self, Given_Salary):
    pattern = re.compile(r'[0-9]{2,3}')
    if pattern.match(Given_Salary):
        try:
            return True
        except ValueError as e:
            return Given_Salary, e

    def val_birthday(self, data):
        self.clean.clean_birthday(data)
        return True
