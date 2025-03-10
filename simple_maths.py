""" This program will ask the user for their name and their favourite numbers
    and then perform some simple maths on their numbers """

# Ask the user for their name and favourite numbers
name = input('What is your name? ')
try:
    n1 = int(input('What is your favourite number? '))
    n2 = int(input('What is your second favourite number? '))
except ValueError:
    print('Please enter an integer')

# Perform some simple maths on the numbers
add = n1 + n2
multiply = n1 * n2

# Greet the user and print the results
print(f'Hi {name}, here are some fun calculations with your favourite numbers!')
print(f'{n1} + {n2} = {add}')
print(f'{n1} * {n2} = {multiply}')