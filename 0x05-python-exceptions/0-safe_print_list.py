#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int) : The number of elemnts of my_list to print.
    Returns:
        The real number of elements printed.
    """
    count = 0
    for num in range(x):
        try:
            print("{}".format(my_list[num]), end="")
        except IndexError:
            break
        else:
            count += 1
    print()
    return (count)count = 0
