''' This program asks the user how many cheese, chicken, pepperoni, and veggie pizzas they want '''

# Defines the list for all the pizzas and number of them
pizzas = ['cheese', 'chicken', 'pepperoni', 'veggie']
number = []

# Goes through all the different types of pizzas and asks the user how many of each they want
for item in pizzas:
    while True:
        try:
            amount = int(input(f'How many {item} pizzas do we want? '))
            if amount < 0:
                print('Please enter a valid amount')
            else:
                number.append(amount)
                break
        except ValueError:
            print('Please enter a valid amount')

# Goes through all the pizzas and print how many the user ordered unless it's 0
for i in range(len(pizzas)):
    if number[i] != 0:
        print(f'{pizzas[i].title()}: {number[i]}')