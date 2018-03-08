class Cleaner(object):

    def clean_empid(self, data):
        result = data.upper()
        return result

    def clean_gender(self, data):
        result = data.upper()
        if (result == "MALE"):
            result = "M"
        if (result == "FEMALE"):
            result = "F"
        return result

    def clean_age(self, data):
        pass

    def clean_sales(self, data):
        pass

    def clean_bmi(self, data):
        return data.capitalize()

    def clean_salary(self, data):
        pass

    def clean_birthday(self, data):
        pass

