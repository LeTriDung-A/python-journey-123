"""Chay vi du OOP cua Week 14."""

from models import BankAccount, Course, SavingsAccount, Student


def main() -> None:
    python = Course("Python", 3)
    database = Course("Co so du lieu", 4)

    student = Student("Dung")
    student.enroll(python)
    student.enroll(database)
    print(student)
    for course in student.courses:
        print("-", course)

    account = BankAccount("Dung", 500_000)
    account.deposit(100_000)
    account.withdraw(50_000)
    print(account)

    savings = SavingsAccount("Dung", 1_000_000, 0.05)
    savings.add_interest()
    print(savings)


if __name__ == "__main__":
    main()
