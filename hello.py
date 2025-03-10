# Asks for name
name = input('What is your name? ').title()
print(f'Hello {name}, nice to meet you!')

try:
    # Asks for age
    age = int(input(f'How old are you {name}? '))

    # Checks for positive integer
    if age <= 0:
        print('Please enter in a positive integer.')

# Checks if it is a number
except ValueError:
    print('Please enter a positive integer.')

if age == 15:
    print('Great age!')
else:
    print('Lame')

# a sss