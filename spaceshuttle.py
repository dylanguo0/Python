''' This program asks the user for a descent speed of a space shuttle until they type in 'conclude'. If the user user enters an invalid input, the program will
    print 'Error, invalid input', and ask again. After the user types in conclude, it'll print out all the unsafe speeds, which are speeds faster than 10m/s'''

# Defines the unsafe speed and break loop condition
UNSAFE = 10
BREAK_LOOP = 'conclude'

# Defines the list which contains all the unsafe speeds
unsafe_speeds = []

# Keeps asking the user for a speed until they enter 'conclude'
while True:

    # Keeps asking the user for a speed until they enter a valid input
    while True:
        try:
            speed = input('Input descent speed in m/s: ')
            if speed != BREAK_LOOP:
                speed = float(speed)
            break
        except ValueError:
            print('Error, invalid input.')
    
    # Breaks the loop if the user entered 'conclude'
    if speed == BREAK_LOOP:
        break

    # Adds it to the list of unsafe speeds if it is unsafe
    if speed > UNSAFE:
        unsafe_speeds.append(speed)

# Show how many unsafe speeds there were and print all the unsafe speeds
print(f'There were {len(unsafe_speeds)} space shuttles faster than the safe speed.')
print('The unsafe speeds are')
for speed in unsafe_speeds:
    print(speed)