import unittest
from Cleaner import Cleaner
from Validator import Validator
import Reader

class CleanerTests(unittest.TestCase):

    def setUp(self):
        # be executed before each test
        self.x = 5

    def tearDown(self):
        # be executed after each test case
        pass #print('down')

    def test_cleaner_empid(self):
        clean = Cleaner()
        test_data = 'A102'
        expected_result = 'A102'

        actual_result = clean.clean_empid(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_empid_2(self):
        clean = Cleaner()
        test_data = 'a102'
        expected_result = 'A102'

        actual_result = clean.clean_empid(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_gender(self):
        clean = Cleaner()
        test_data = 'male'
        expected_result = 'M'

        actual_result = clean.clean_gender(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_gender_2(self):
        clean = Cleaner()
        test_data = 'm'
        expected_result = 'M'

        actual_result = clean.clean_gender(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_gender_3(self):
        clean = Cleaner()
        test_data = 'female'
        expected_result = 'F'

        actual_result = clean.clean_gender(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_gender_4(self):
        clean = Cleaner()
        test_data = 'f'
        expected_result = 'F'

        actual_result = clean.clean_gender(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_bmi(self):
        clean = Cleaner()
        test_data = 'normal'
        expected_result = 'Normal'

        actual_result = clean.clean_bmi(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_bmi_2(self):
        clean = Cleaner()
        test_data = 'UNDERWEIGHT'
        expected_result = 'Underweight'

        actual_result = clean.clean_bmi(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_bmi_3(self):
        clean = Cleaner()
        test_data = 'overweight'
        expected_result = 'Overweight'

        actual_result = clean.clean_bmi(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

    def test_cleaner_bmi_4(self):
        clean = Cleaner()
        test_data = 'OBEsity'
        expected_result = 'Obesity'

        actual_result = clean.clean_bmi(test_data)

        self.assertEqual(actual_result, expected_result, "actaul_result should equil" + expected_result)

class ValidatorTests(unittest.TestCase):

    def test_validator_empid_true(self):
        val = Validator()
        employee_place_holder = ''
        test_data = 'A201'
        actual_result = val.val_empid(employee_place_holder, test_data)

        self.assertTrue(actual_result)

    def test_validator_empid_false(self):
        val = Validator()
        employee_place_holder = ''
        test_data = 'AA01'
        actual_result, error_message = val.val_empid(employee_place_holder, test_data)

        self.assertFalse(actual_result, error_message)

    def test_validator_empid_false_2(self):
        val = Validator()
        employee_place_holder = ''
        test_data = '3201'
        actual_result, error_message = val.val_empid(employee_place_holder, test_data)

        self.assertFalse(actual_result, error_message)

    def test_validator_gender_true(self):
        val = Validator()
        test_data = 'M'
        actual_result, error_message = val.val_gender(test_data)

        self.assertTrue(actual_result, error_message)

    def test_validator_gender_true_2(self):
        val = Validator()
        test_data = 'F'
        actual_result, error_message = val.val_gender(test_data)

        self.assertTrue(actual_result, error_message)

    def test_validator_gender_false(self):
        val = Validator()
        test_data = 'other'
        actual_result, error_message = val.val_gender(test_data)

        self.assertFalse(actual_result, error_message)

    def test_validator_gender_false(self):
        val = Validator()
        test_data = 'other'
        actual_result, error_message = val.val_gender(test_data)

        self.assertFalse(actual_result, error_message)

    def test_validator_bmi_true(self):
        val = Validator()
        data = 'Normal', 'Underweight', 'Obesity', 'Overweight'
        for x in data:
            actual_result, error_message = val.val_bmi(x)
            self.assertTrue(actual_result, error_message)

    def test_validator_bmi_false(self):
        val = Validator()
        data = 'other'
        for x in data:
            actual_result, error_message = val.val_bmi(x)
            self.assertFalse(actual_result, error_message)

if __name__ == '__main__':
    unittest.main()