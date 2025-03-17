''' This program asks the user how many cheese, chicken, pepperoni, and veggie pizzas they want '''

# Defines the list for all the pizzas and number of them
pizzas = ['cheese', 'chicken', 'pepperoni', 'veggie']
number = []

# Goes through all the different types of pizzas and asks the user how many of each they want
for item in pizzas:
    number.append(int(input(f'How many {item} pizzas do we want? ')))

# Goes through all the pizzas and print how many the user ordered unless it's 0
for i in range(len(pizzas)):
    if number[i - 1] != 0:
        print(f'{pizzas[i - 1].title()}: {number[i - 1]}')