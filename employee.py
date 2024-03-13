class Employee:
    """Create an employee object."""

    def __init__(self, first, last, salary):
        """Create an employee with first and last names and salary attributes."""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, bump=5000):
        """Adds $5k to salary by default or accepts a custom amount."""
        self.salary = self.salary + bump
