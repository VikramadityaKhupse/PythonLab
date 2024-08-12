def pattern(n):
    height = 2 * n + 1
    mid = height // 2

    # Upper part
    for i in range(mid):
        for j in range(mid - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Center
    print("*" + " " * (mid - 1) + str(n) + " " * (mid - 1) + "*")

    # Lower part
    for i in range(mid - 1, -1, -1):
        for j in range(mid - i):
            if i == 0:
                pass
            else:
                print(" ", end="")
        for j in range(2 * i + 1):

            if i == 0:
                for i in range(n):
                    print("*" * height, end="\n")
                else:
                    print(" ", end="")
            else:
                if j == 0 or j == 2 * i:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()


pattern(1)
