''' This program will ask the user how many times to roll a die and the max face on it 
    then calculate the percent of the time a number appeared'''

import random

# Defines the list
rolls = []

# Asks the user for the amount of times to roll the die and the max face
# then check it's a positive integer
while True:
    try:
        times = int(input('How many times to roll the die: '))
        if times > 0:
            break
        else:
            print('Please enter a positive integer')
    except:
        print('Please enter a positive integer')

while True:
    try:
        maximum = int(input('Max face on the die: '))
        if maximum > 0:
            break
        else:
            print('Please enter a positive integer')
    except:
        print('Please enter a positive integer')

# Rolls the die the amount of times inputted by the user
for i in range(times):
    rolls.append(random.randint(1, maximum))

# Checks how many times a number appeared then converts it to a percentage
for i in range(maximum):
    print(f'{i + 1} appeared {round((rolls.count(i + 1) / times * 100), 2)}% of the time.')