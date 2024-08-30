def print_pattern(num):
    for i in range(num):
        for s in range(num, i+1, -1):
            print(" ", end="")
        for j in range(i+1):
            print("*",end="")
        for j in range(i):
            print("*",end="")
        print()
    

print_pattern(5)