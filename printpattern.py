# def printpattern(len):
#     if len < 1:
#         return "Enter positive number"
#     elif len % 10 != 0.0:
#         return "Enter positive integer value"
#     elif len % 10 == 0.0:
#         return "Work in progress"
#
#
def printpattern(n):
    rows = n * 2
    s1 = rows + n if n % 2 == 0 else rows + n - 1
    s2 = 0
    array = []
    for i in range(rows):
        row = i + 1
        s1 -= 2 + 1 - i
        s2 += row
        array.append([row, s1, s2])

    for row, s1, s2 in array:
        print(row, s1, s2)
        if row == 1:
            print(" " * s1 + " * " * 0 + " " * s2 + "*" + " " * s2 + " * " * 0 + " " * s1)
        elif row == n + 1:
            print(" " * s1 + " * " * 1 + " " * s2 + str(n) + " " * s2 + " * " * 1 + " " * s1)
        elif row < n + 1:
            print(" " * s1 + " * " * 1 + " " * s2 + " " + " " * s2 + " * " * 1 + " " * s1)


printpattern(2)
# # if n = 3:
# print(" "*8+" * "*0+" "*0+"*"+" "*0+" * "*0+" "*8)
# print(" "*5+" * "*1+" "*1+" "+" "*1+" * "*1+" "*8)
# print(" "*3+" * "*1+" "*3+" "+" "*3+" * "*1+" "*3)
# print(" "*2+" * "*1+" "*4+"3"+" "*4+" * "*1+" "*2)
# print(" "*3+" * "*1+" "*3+" "+" "*3+" * "*1+" "*3)
# print(" "*5+" * "*1+" "*1+" "+" "*1+" * "*1+" "*8)
# print(" *"*4+" * "+"* "*4)
# print(" *"*4+" * "+"* "*4)
# print(" *"*4+" * "+"* "*4)
#
# # if n = 2
# print(" "*6+" * "*0+" "*0+"*"+" "*0+" * "*0+" "*6)
# print(" "*3+" * "*1+" "*1+" "+" "*1+" * "*1+" "*3)
# print(" "*1+" * "*1+" "*3+"2"+" "*3+" * "*1+" "*1)
# print(" "*3+" * "*1+" "*1+" "+" "*1+" * "*1+" "*3)
# print(" *"*3+" * "+"* "*3)
# print(" *"*3+" * "+"* "*3)
