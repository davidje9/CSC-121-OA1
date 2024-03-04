"""Applied both book exercises 10-13 and 10-14:
    10-13: store user info as a dictionary
    10-14: verify user before greeting
Note that moodle assigned the steps of ex 10-14 but mislabeled it 10-13."""

from pathlib import Path
import json
import sys

def get_stored_user_name(path):
    """Get stored username from the json dictionary."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info['user_name'] 

def get_new_user_name(path):
    """Prompt a new user to enter their user information."""
    print("It appears to be your first time here. To create a new username, please enter the following information.")
    first_name = input("Enter your first name:  ")
    last_name = input("Enter your last name:  ")
    team_name = input("What team are you on? (Amate/Star Content/AR Content/Other)  ")
    user_name = first_name[0:2] + last_name[0:5]
    user_info = {'user_name': user_name, 'last_name': last_name, 'first_name': first_name, 'team_name': team_name}
    print(f"Nice to meet you! Your username will be {user_name}.")
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_name

def verify_user():
    """Verify returning user's username."""
    unverified = True
    path = Path('user_info.json')
    user_name = get_stored_user_name(path)
    while unverified:
        verified = input(f"Is your username {user_name}? (y/n, or q to quit)  ")
        if verified.lower() == 'y' or verified.lower() == 'yes':
            unverified = False
            return unverified
        elif verified.lower() == 'n' or verified.lower() == 'no':
            user_name = get_new_user_name(path)
            unverified = False
            return unverified
        elif verified.lower() == 'q' or verified.lower() == 'quit':
            print("User verification canceled.")
            exit_program()
        else:
            print("\nPlease enter only y, n, or q (yes, no, or quit).\n")

def exit_program():
    print("Good bye!")
    sys.exit(0)

def greet_user():
    """Greet user by username."""
    path = Path('user_info.json')
    user_name = get_stored_user_name(path)
    if user_name:
        unverified = verify_user()
    else:
        get_new_user_name(path)
    user_name = get_stored_user_name(path)
    print(f"Welcome to the application, {user_name}!")

greet_user()
