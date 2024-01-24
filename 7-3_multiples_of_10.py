number = input("Enter a whole number to check whether it is divisible by 10:  ")
if number.isnumeric():
    number = int(number)
    if number % 10 == 0:
        print(f"\nThe number {number} is divisible by 10.")
    else:
        print(f"\nThe number {number} is not divisible by 10.")
else:
    print("Invalid entry. Please enter a valid number.")
