#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Exclude the script name
    count = len(argv)

    # Print the header line
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Print each argument with its position
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i]))
