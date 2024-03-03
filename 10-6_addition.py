print("\nWelcome to my homework for exercise 10-6: Addition!")
print("---------------------------------------------------")

active = "y"

while active == "y":
    while True:
        try:
            number_one = int(input("\nPlease enter your first number:  "))
            break
        except ValueError:
            print("Dear Sir or Madam, I regret to inform you that you cannot perform addition with non-numerical values. Please give it another go. I believe in you!")
    while True:
        try:
            number_two = int(input("Please enter your second number:  "))
            break
        except ValueError:
            print("Dear Sir or Madam, I regret to inform you that you cannot perform addition with non-numerical values. Please give it another go. I believe in you!")

#show results
    sum = number_one + number_two 
    print(f"\n****************\n{number_one} + {number_two} = {sum}")
    active = input("Would you like to continue? (y/n):  ")
print("Thanks for adding with me! It has really been sum-thing!")
