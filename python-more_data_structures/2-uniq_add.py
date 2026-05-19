#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    sorted_list = sorted(my_list)
    empty_list = []
    for i in range(len(sorted_list)):
        if sorted_list[i] not in empty_list:
            empty_list.append(sorted_list[i])

    return sum(empty_list)
