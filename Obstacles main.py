"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    for i in range(3):
        put_one_beeper()
    while front_is_clear():
        move()


def put_one_beeper():
    while not_facing_west():
        safe_move()
    turn_around()
    move()
    turn_right()
    while front_is_clear():
        safe_move()
    turn_left()
    put_beeper()


def safe_move():
    if front_is_blocked():
        turn_left()
    else:
        move()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()