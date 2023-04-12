import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('fahim', 'chowdhury', 50000)
        self.emp_2 = Employee('farmida', 'chowdhury', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'fahim.chowdhury@email.com')
        self.assertEqual(self.emp_2.email, 'farmida.chowdhury@email.com')

        self.emp_1.first = 'hridi'
        self.emp_2.first = 'hritri'

        self.assertEqual(self.emp_1.email, 'hridi.chowdhury@email.com')
        self.assertEqual(self.emp_2.email, 'hritri.chowdhury@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'fahim chowdhury')
        self.assertEqual(self.emp_2.fullname, 'farmida chowdhury')

        self.emp_1.first = 'hridi'
        self.emp_2.first = 'hritri'

        self.assertEqual(self.emp_1.fullname, 'hridi chowdhury')
        self.assertEqual(self.emp_2.fullname, 'hritri chowdhury')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/chowdhury/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/chowdhury/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()