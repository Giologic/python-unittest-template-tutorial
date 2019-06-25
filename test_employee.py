import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    print('setupClass\n')

  @classmethod
  def tearDownClass(cls):
    print('teardownClass')

  def setUp(self):
    print('setup')
    self.emp_1 = Employee('Darth', 'Vader', 50000)
    self.emp_2 = Employee('Storm', 'Trooper', 60000)

  def tearDown(self):
    print('teardown\n')

  def test_email(self):
    print('test_email')

    self.assertEqual(self.emp_1.email, 'Darth.Vader@email.com')
    self.assertEqual(self.emp_2.email, 'Storm.Trooper@email.com')

    self.emp_1.first = 'John'
    self.emp_2.first = 'Doe'

    self.assertEqual(self.emp_1.email, 'John.Vader@email.com')
    self.assertEqual(self.emp_2.email, 'Doe.Trooper@email.com')

  def test_fullname(self):
    print('test_fullname')

    self.assertEqual(self.emp_1.fullname, 'Darth Vader')
    self.assertEqual(self.emp_2.fullname, 'Storm Trooper')

    self.emp_1.first = 'John'
    self.emp_2.first = 'Doe'

    self.assertEqual(self.emp_1.fullname, 'John Vader')
    self.assertEqual(self.emp_2.fullname, 'Doe Trooper')

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
      mocked_get.assert_called_with('http://company.com/Vader/May')
      self.assertEqual(schedule, 'Success')

      mocked_get.return_value.ok = False

      schedule = self.emp_2.monthly_schedule('June')
      mocked_get.assert_called_with('http://company.com/Trooper/June')
      self.assertEqual(schedule, 'Bad Response')


if __name__ == "__main__":
  unittest.main()