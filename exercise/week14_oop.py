"""Vi du OOP don gian cho bai tap Week 14."""


class Course:
    def __init__(self, name: str, credits: int):
        if not name.strip():
            raise ValueError("Ten mon hoc khong duoc de trong.")
        if credits <= 0:
            raise ValueError("So tin chi phai lon hon 0.")
        self.name = name.strip()
        self.credits = credits

    def __str__(self) -> str:
        return f"{self.name} ({self.credits} tin chi)"


class Student:
    """Student co danh sach Course, minh hoa composition."""

    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Ten sinh vien khong duoc de trong.")
        self.name = name.strip()
        self.courses: list[Course] = []

    def enroll(self, course: Course) -> None:
        if not isinstance(course, Course):
            raise TypeError("course phai la mot Course.")
        if course not in self.courses:
            self.courses.append(course)

    def total_credits(self) -> int:
        return sum(course.credits for course in self.courses)

    def __str__(self) -> str:
        return f"{self.name}: {len(self.courses)} mon, {self.total_credits()} tin chi"


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        if not owner.strip():
            raise ValueError("Ten chu tai khoan khong duoc de trong.")
        if balance < 0:
            raise ValueError("So du ban dau khong duoc am.")
        self.owner = owner.strip()
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("So tien nap phai lon hon 0.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("So tien rut phai lon hon 0.")
        if amount > self.balance:
            raise ValueError("So du khong du.")
        self.balance -= amount

    def __str__(self) -> str:
        return f"{self.owner}: {self.balance:.2f} VND"


class SavingsAccount(BankAccount):
    """SavingsAccount la mot BankAccount co them lai suat."""

    def __init__(self, owner: str, balance: float = 0, interest_rate: float = 0.03):
        super().__init__(owner, balance)
        if interest_rate < 0:
            raise ValueError("Lai suat khong duoc am.")
        self.interest_rate = interest_rate

    def add_interest(self) -> None:
        self.balance += self.balance * self.interest_rate


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
