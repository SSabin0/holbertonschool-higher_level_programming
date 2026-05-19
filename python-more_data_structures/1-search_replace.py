def search_replace(my_list, search, replace):
    """Replaces all occurrences using a list comprehension."""
    return [replace if x == search else x for x in my_list]
