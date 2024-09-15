"""
Homework 04 - JailBreak

Student: YOUR NAME
Semester: YOUR SEMESTER

This assignment focuses on learning while loops. It
is inspired by

Think Like a Coder ep1 Lesson by Alex Rosenthal, directed by Kozmonot Animation Studio.

https://www.youtube.com/watch?v=KFVdHDMcepw&list=PLJicmE8fK0EgogMqDYMgcADT1j5b911or&index=2
"""
from random import randint
from lock_tools import COMBO, PATTERN, MAX_PATTERN_SIZE, check_solution, is_open, \
    get_lock_type, new_door, get_single_combo, get_single_pattern
# by importing these functions and variables, you can use them directly in your code
# for example:
#  if get_lock_type(val) == COMBO:
#      do something


def check_combo_lock(lock_id: int) -> int:
    """
    Checks possible combinations for a combo lock, until
    the correct solution is found.

    Args:
        lock_id (int): the lock to check

    Returns:
        (int): the solution to the lock, or minus 1 if not found
    """
    pass

def check_pattern_lock(lock_id: int) -> str:
    """
    Checks possible patterns for a pattern lock, until
    the correct solution is found.

    Args:
        lock_id (int): the lock to check

    Returns:
        str: The pattern solution to the lock
    """
    pass


def open_door(num_locks: int) -> bool:
    """
    Opens a door with a number of locks. The door is opened by
    guessing the correct solution to each lock.

    Args:
        num_locks (int): the number of locks on the door

    Returns:
        bool: True if the door is opened, False otherwise
    """

    # Optional - you  may find it useful adding this, your variable names may differ
    # print(__FEEDBACK_MESSAGE.format(lock_type=lock_type, lock_id=lock_id, solution=final))
    return is_open()


def main():
    """ Starting point for the program. """
    print(__WELCOME_MESSAGE)
    total_doors = randint(1, 6)  # generate a random number of doors
    counter = 0
    while counter < total_doors:
        locks = new_door()
        print(__OPENING_DOOR_MESSAGE.format(counter=counter + 1, locks=locks))
        if not open_door(locks):
            print(__TRAPPED_MESSAGE)
            return
        counter += 1
    print(__GOODBYE_MESSAGE)


__WELCOME_MESSAGE = """Hello explorer! You have been captured and placed in a jail cell.
The only way to escape is to open the door. Make use of your infobot to help you escape."""
__GOODBYE_MESSAGE = "Congratulations! You have escaped the jail cell. You are now free."
__OPENING_DOOR_MESSAGE = "Opening door number: {counter} with {locks} locks."
__TRAPPED_MESSAGE = "You have been trapped. Better luck next time. (check for errors in your code)"
__FEEDBACK_MESSAGE = "Opened lock {lock_type} {lock_id} with solution\n{solution}"


if __name__ == "__main__":
    main()
