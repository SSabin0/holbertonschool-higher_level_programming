#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Get arguments excluding the script name
    argv = sys.argv[1:]
    count = len(argv)

    # Logic for header punctuation and pluralization
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Print each argument with its 1-based index
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i]))
