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

    def val_sales(self, data):
        self.clean.clean_sales(data)
        return True

    def val_bmi(self, data):
        data = self.clean.clean_bmi(data)
        if data == 'Normal' or data == 'Overweight' or data == 'Obesity' or data == 'Underweight':
            return True
        else:
            return False

    def val_salary(self, data):
        self.clean.clean_salary(data)
        return True

    def val_birthday(self, data):
        self.clean.clean_birthday(data)
        return True
