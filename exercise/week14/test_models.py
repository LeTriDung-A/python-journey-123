"""Unit test co ban cho cac lop Week 14."""

import unittest

from models import BankAccount, Course, SavingsAccount, Student


class TestCourseAndStudent(unittest.TestCase):
    def test_student_total_credits(self):
        student = Student("Dung")
        student.enroll(Course("Python", 3))
        student.enroll(Course("SQL", 4))
        self.assertEqual(student.total_credits(), 7)

    def test_course_rejects_invalid_credits(self):
        with self.assertRaises(ValueError):
            Course("Python", 0)


class TestBankAccount(unittest.TestCase):
    def test_deposit_and_withdraw(self):
        account = BankAccount("Dung", 100)
        account.deposit(50)
        account.withdraw(30)
        self.assertEqual(account.balance, 120)

    def test_withdraw_more_than_balance(self):
        account = BankAccount("Dung", 100)
        with self.assertRaises(ValueError):
            account.withdraw(101)

    def test_savings_interest(self):
        account = SavingsAccount("Dung", 1000, 0.1)
        account.add_interest()
        self.assertAlmostEqual(account.balance, 1100)


if __name__ == "__main__":
    unittest.main()
