from Cleaner import Cleaner
from Validator import Validator


class Controller(object):

    val = Validator()
    clean = Cleaner()

    def test_empid(self):
        data = "a001"
        print(self.clean.clean_empid(data))
        print(self.val.val_empid(self.clean.clean_empid(data)))

    def test_gender(self):
        data = 'female'
        print(self.clean.clean_gender(data))
        print (self.val.val_gender(self.clean.clean_gender(data)))

    def test_bmi(self):
        data = 'normal'
        print(self.clean.clean_bmi(data))
        print(self.val.val_bmi(self.clean.clean_bmi(data)))

control = Controller()
control.test_empid()
