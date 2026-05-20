#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not a_dictionary:
        return None

    best_key = None
    max_score = float('-inf')  # Starts at the lowest possible value

    for key, score in a_dictionary.items():
        if score > max_score:
            max_score = score
            best_key = key

    return best_key
