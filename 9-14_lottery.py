from random import choice

#tuples for the 10 numbers and 5 letters that may be pulled for the lotto
#lotto_characters = (0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e')
lotto_numbers = (0,1,2,3,4,5,6,7,8,9)
lotto_letters = ('a','b','c','d','e')

#randomly generate tuple winning_ticket consisting of 4 numbers + 1 letter
winning_ticket = (str(choice(lotto_numbers)), str(choice(lotto_numbers)), str(choice(lotto_numbers)), str(choice(lotto_numbers)), str(choice(lotto_letters)))

winning_ticket = sorted(winning_ticket)

#initialize prompts and variable to get user input to form the user_ticket
prompt_number = "Choose your first number! (0-9)"
prompt_letter = "Now choose a winning letter. (a-e)"
user_ticket = ('')

#while loop to run until the user ticket has 4 numbers and handle user errors
#try/except for non-integer input error & if/else for out-of-range input error
while len(user_ticket) < 4:
    user_selection = input(prompt_number)
    try:
        user_selection = int(user_selection)
        if 0 <= user_selection <=9:
            user_ticket += str(user_selection)
            prompt_number = "Choose another number! (0-9)"
        else:
            print("Your number is out of range. Please choose a single-digit number from 0-9.")
    except ValueError:
            print("Error. Please choose a single-digit number from 0-9.")

#while True loop to get correct user input on letter
while True:
    user_selection = input(prompt_letter)
    user_selection = user_selection.lower()
    if user_selection == 'a' or user_selection == 'b' or user_selection == 'c' or user_selection == 'd' or user_selection == 'e':
        user_ticket += (user_selection)
        break
    else:
        print("Please enter only a letter from a-e.")

user_ticket = sorted(user_ticket)

#compare user_ticket to winning_ticket and print results
result = ""
if user_ticket == winning_ticket:
    result = "CONGRATULATIONS! You won a prize!\n"
else:
    result = "Your ticket did not win. Better luck next time!\n"

print(f"\n--------------\nThe winning combination is... {winning_ticket}.\nYour ticket shows {user_ticket}.\n--------------\n{result}")
