''' This program asks the user for a descent speed of a space shuttle until they type in 'conclude'. If the user user enters an invalid input, the program will
    print 'Error, invalid input', and ask again. After the user types in conclude, it'll print out all the unsafe speeds, which are speeds faster than 10m/s'''

# Defines the unsafe speed and break loop condition
UNSAFE = 10
BREAK_LOOP = 'conclude'

# Defines the list which contains all the unsafe speeds
unsafe_speeds = []

# Asks the user for a speed
speed = input('Input descent speed in m/s: ')

# Keeps asking the user for a speed until they enter 'conclude'
while speed != BREAK_LOOP:

    # Keeps asking the user for a speed until they enter a valid input
    try:
        speed = float(speed)
        if speed > UNSAFE:
            unsafe_speeds.append(speed)
    except ValueError:
        print('Error, invalid input.')

    # Asks the user for a speed
    speed = input('Input descent speed in m/s: ')

# Show how many unsafe speeds there were and print all the unsafe speeds
if len(unsafe_speeds) != 1:
    print(f'There were {len(unsafe_speeds)} space shuttles faster than the safe speed.')
    if len(unsafe_speeds) != 0:
        print('The unsafe speeds are')
        for speed in unsafe_speeds:
            print(speed)
else:
    print(f'There was 1 space shuttle faster than the safe speed.\nThe unsafe speed is\n{unsafe_speeds[0]}')