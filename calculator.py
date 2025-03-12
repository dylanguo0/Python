''' This program asks the user for 2 numbers and an operator then calculates the answer '''

# Function for calculator
def calculate(n1, operator, n2):
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    elif operator == '*':
        return n1 * n2
    elif operator == '/':
        return n1 / n2
    elif operator == '^':
        return n1 ** n2

# Asks the user for the 2 numbers and check it's a number
while True:
    try:
        n1 = float(input('Enter a number: '))
        break
    except ValueError:
        print('Please enter a number')

while True:
    try:
        n2 = float(input('Enter another number: '))
        break
    except ValueError:
        print('Please enter a number')

# Asks the user for an operator and check it's valid
while True:
    operator = input('Enter an operator (+, -, *, /, ^): ')
    if operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '^':
        print('Please enter a valid operator')
    else:
        break

# Calculates it while checking for any errors
try:
    print(calculate(n1, operator, n2))
except OverflowError:
    print('Answer is > 1.79e+308')
except ZeroDivisionError:
    print('Please don\'t divide by 0')