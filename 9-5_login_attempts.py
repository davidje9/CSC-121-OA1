class User:
    """Basic user attributes for a simple website."""
    def __init__(self, first_name, last_name, pin, access_level, dob_day, dob_month, dob_year):
        self.first_name = first_name
        self.last_name = last_name
        self.pin = pin
        self.access_level = access_level
        self.dob_day = dob_day
        self.dob_month = dob_month
        self.dob_year = dob_year
        self.login_attempts = 0
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} was born {self.dob_month}/{self.dob_day}/{self.dob_year}. Their pin is {self.pin}, which grants {self.access_level} access.")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")
    def increment_login_attempts(self):
        """Increments the login attempts by 1."""
        self.login_attempts += 1
    def reset_login_attempts(self):
        """Resets the user's login attempts to 0."""
        self.login_attempts = 0

#instantiate a user
user_0000 = User('david', 'everson', 1234, 'admin', 30, 8, 1978)
user_0000.greet_user()
user_0000.describe_user()

#increment login attempts several times before resetting
user_0000.increment_login_attempts()
print(user_0000.login_attempts)
user_0000.increment_login_attempts()
print(user_0000.login_attempts)
user_0000.increment_login_attempts()
print(user_0000.login_attempts)
user_0000.increment_login_attempts()
print(user_0000.login_attempts)
user_0000.reset_login_attempts()
print(user_0000.login_attempts)
