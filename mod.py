def modulo(num1, num2):
    if num2 == 0:
        raise ValueError("Division by zero is undefined.")
    else:
        quo = num1 // num2
        return num1 - quo * num2


print(modulo(15, 4))
