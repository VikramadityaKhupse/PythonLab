def printpattern(len):
    if len < 1:
        return "Enter positive number"
    elif len % 10 != 0.0:
        return "Enter positive integer value"
    elif len % 10 == 0.0:
        return "Work in progress"


def pattern(rows):
    rows += 2
    for i in range(1, rows + 1):
        print(" " * (rows + 2) + " * " * (2 * i - 1))
        rows -= 1



pattern(1)
