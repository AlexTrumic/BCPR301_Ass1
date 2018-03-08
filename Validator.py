from Cleaner import Cleaner

class Validator(object):

    clean = Cleaner()

    def val_gender(self, data):
        data = self.clean.clean_gneder(data)
        if data == 'M' or 'F':
            return True
        else:
            return False

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

    def val_bmi(self, data):
        data = self.clean.clean_bmi(data)
        if data == 'Normal' or 'Overweight' or 'Obesity' or 'Underweight':
            return True
        else:
            return False
