#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int) : The number of elemnts of my_list to print.
    Returns:
        The real number of elements printed.
    """
    sum = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            sum += 1
        except IndexError:
            break
    print("")
    return (sum)
