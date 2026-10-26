"""Exercise 01: class, object and methods."""


class Progress:
    def __init__(self, completed: int, total: int):
        if total < 1:
            raise ValueError("total must be positive")
        if completed < 0 or completed > total:
            raise ValueError("completed must be between 0 and total")

        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


def main() -> None:
    progress = Progress(3, 4)
    print(progress)
    print(f"Percentage: {progress.percentage()}%")


if __name__ == "__main__":
    main()
