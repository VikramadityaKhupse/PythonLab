




def printPattern(n):
    rows = 2 * n + 1

    for i in range(rows - 1):

        print()
        for j in range(rows - i):
            print(" ", end="")

        for k in range(1, 2 * i):

            if i == n + 1 and k == n + 1:
                print("*", end="")
            else:
                # print(i, end = "")
                print("+", end="")
    for i in range(rows - 2):
        print()
        for j in range(rows-n):
            print(" ", end="")
        for k in range(2 * i, rows - 2):
            print("+", end="")


printPattern(2)
