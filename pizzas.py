''' This program asks the user how many cheese, chicken, pepperoni, and veggie pizzas they want '''

# Defines the list for all the pizzas and number of them
pizzas = ['cheese', 'chicken', 'pepperoni', 'veggie']
number = []

for item in pizzas:
    number.append(int(input(f'How many {item} pizzas do we want? ')))

for i in range(len(pizzas)):
    print(f'{pizzas[i - 1].title()}: {number[i - 1]}')