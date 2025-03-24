''' This program asks the user for a descent speed of a space shuttle until they type in 'conclude'. If the user user enters an invalid input, the program will
    print 'Error, invalid input', and ask again. After the user types in conclude, it'll print out all the unsafe speeds, which are speeds faster than 10m/s'''

# Defines the unsafe speed
UNSAFE = 10
BREAK_LOOP = 'conclude'

# Defines the list which contains all the unsafe speeds
unsafe_speeds = []

# Keeps asking the user for a speed until they enter 'conclude'
while True:
    speed = input('Input descent speed in m/s: ')
    if speed == BREAK_LOOP:
        break
    else:
        speed = float(speed)
    if speed > UNSAFE:
        unsafe_speeds.append(speed)