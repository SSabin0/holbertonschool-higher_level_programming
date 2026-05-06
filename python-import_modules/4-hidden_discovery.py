#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Use dir() to get all names in the module
    names = dir(hidden_4)

    # Filter and sort the names
    # Only keep names that do NOT start with "__"
    filtered_names = [name for name in names if not name.startswith("__")]
    filtered_names.sort()

    # Print one per line
    for name in filtered_names:
        print(name)
