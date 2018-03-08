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

    def clean_bmi(self, data):
        return data.capitalize()
