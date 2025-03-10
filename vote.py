''' This program will aks the user for their name, age, and if they are a resident of New Zealand,
    then it will figure out if the user can vote in New Zealand '''

# Sets the voting age
VOTING_AGE = 18

# Asks for the user's name and check that it's not empty
name = input('What is your name? ').title().lstrip(' ')
while name == '':
    print('Please enter a name')
    name = input('What is your name? ').title().lstrip(' ')

# Asks for the user's age and checks if it's a positive integer
while True:
    try:
        age = int(input('What is your age? '))
        if age < 0:
            print('Please enter a valid integer')
        else:
            break
    except ValueError:
        print('Please enter a valid integer')

# Asks if the user is a resident of New Zealand and checks if they entered yes or no
while True:
    residency = input('Are you a resident of New Zealand (yes/no)? ').lower()
    if 'yes' not in residency and 'no' not in residency:
        print('Please enter yes or no')
    else:
        break

# Checks and tells if the user can vote
if age >= VOTING_AGE and residency == 'yes':
    print(f'{name}, you are allowed to vote in New Zealand!')
else:
    print(f'Sorry {name}, you are not allowed to vote in New Zealand.')