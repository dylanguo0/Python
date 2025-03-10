''' This program will check to see if the user as entered a valid integer 
within a specific range of values'''

# Use constants for the minimum and maximum values
MIN = 1
MAX = 10

# Asks the user to enter a number
num = input('Enter a number: ')

# Check to see if the number is valid
if num.lstrip('-').isnumeric():
    num = int(num)
    if num < MIN:
        print(f'{num} is lower than {MIN}')
    elif num > MAX:
        print(f'{num} is higher than {MAX}')
    else:
        print(f'Your number is {num}')
else:
    print(f'{num} is not an integer')