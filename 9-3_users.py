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
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} was born {self.dob_month}/{self.dob_day}/{self.dob_year}. Their pin is {self.pin}, which grants {self.access_level} access.")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")

#Instantiate four User objects
user_0000 = User('david', 'everson', 1234, 'admin', 30, 8, 1978)
user_0001 = User('megan', 'hoak', 4321, 'edit', 20, 5, 1986)
user_0002 = User('kris', 'phillips', 6789, 'read only', 26, 12, 1977)
user_0003 = User('kevin', 'fitzgerald', 9876, 'read only', 29, 8, 1979)
              
#Call methods for each user
user_0000.describe_user()
user_0001.describe_user()
user_0002.describe_user()
user_0003.describe_user()

user_0000.greet_user()
user_0001.greet_user()
user_0002.greet_user()
user_0003.greet_user()  
