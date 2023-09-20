"""
Python program that takes a token number from the user and checks if the sum of the last two digits is equal to 3 or 8. If it is, it prints "Winner of the lucky draw," otherwise, it prints "Not a winner."

"""

# Input a token number from the user
token_number = input("Enter your token number: ")

# Ensure that the input is at least 2 characters long
if len(token_number) < 2:
    print("Invalid token number. Please enter at least two digits.")
else:
    # Extract the last two digits from the token number
    last_two_digits = token_number[-2:]
    print(last_two_digits)
    # Calculate the sum of the last two digits as an integer
    sum_last_two_digits = int(last_two_digits[0]) + int(last_two_digits[1])

    # Check if the sum is equal to 3
    if sum_last_two_digits == 3 or sum_last_two_digits == 8:
        print("Winner of the lucky draw!")
    else:
        print("Not a winner.")
