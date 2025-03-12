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

operator = 0
while operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '^':
    operator = input('Enter an operator (+, -, *, /, ^): ')

try:
    print(calculate(n1, operator, n2))
except OverflowError:
    print('Answer is > 1.79e+308')
except ZeroDivisionError:
    print('Please don\'t divide by 0')