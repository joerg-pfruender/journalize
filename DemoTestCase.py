import sys
import unittest
import utils
import main

class DemoTestCase(unittest.TestCase):

    def testdemo(self):
        # mock output
        with open('output/output.txt', 'w') as mockStdErr:
            utils.stdErr = mockStdErr

            # given: sample_input.csv

            # when
            main.main('input/sample_input.csv')

            # cleanup
            utils.stdErr = sys.stderr

            # then
            with open('output/income.csv', 'r') as file:
                actual_income = file.read()

            with open('output/expenses.csv', 'r') as file:
                actual_expenses = file.read()

            with open('output/output.txt', 'r') as file:
                actual_error_logs = file.read()

            self.assertEqual(actual_income, '2024-01-01;Transfer;Sample Company;;Salary;DE89370400440532013000;1000.0;EUR;bank_account;regular_income\n'+
    '2024-01-03;Transfer;Some Person;;private gift;DE89370400440532013000;100.0;EUR;bank_account;other_income\n')

            self.assertEqual(actual_expenses, '2024-01-02;Withdraw;;;;;-200;EUR;bank_account;other_expenses\n' +
    '2024-01-04;Transfer;;Grocery Store;Thank you for shopping with us!;DE89370400440532013000;-34.67;EUR;bank_account;other_expenses\n' +
    '2024-01-05;Transfer;;Landlord;Rent;DE89370400440532013000;-500.0;EUR;bank_account;rent\n' +
    '2024-02-05;Transfer;;Person1;private gift;DE02120300000000202051;-50.0;EUR;bank_account;gifts\n' +
    '2024-02-05;Transfer;;Charity;private gift;DE02701500000000594937;-200.0;EUR;bank_account;charity\n' +
    '2024-02-05;Transfer;;Person2;refund expenses;DE02120300000000202051;-42.23;EUR;bank_account;refund\n'
                             )

            self.assertEqual(actual_error_logs, '')

    def test_match_purpose_patterns_is_graceful_when_called_with_wrong_string(self):
        self.assertEqual(True, utils.contains_pattern(['gift'], 'gift'))
        self.assertEqual(True, utils.contains_pattern('gift', 'gift'))
        self.assertEqual(True, utils.contains_pattern(['gift'], 'some gift random'))
        self.assertEqual(True, utils.contains_pattern('gift', 'some gift random'))
        self.assertEqual(True, utils.contains_pattern(['gift'], 'no gift'))
        self.assertEqual(False, utils.contains_pattern('gift', 'refund expenses'))
        self.assertEqual(False, utils.contains_pattern(['gift'], 'refund expenses'))



