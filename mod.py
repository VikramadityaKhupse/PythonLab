def mod(num1, num2):
    while num1 >= num2:
        num1 -= num2
    return num1
print(mod(3, 3))
print(3%3)