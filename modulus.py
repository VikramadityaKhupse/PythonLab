def modulo(num1, num2):
    if num2 == 0:
        raise ValueError("Division by zero is undefined.")


    abs_num1 = abs(num1)
    abs_num2 = abs(num2)

    while abs_num1 >= abs_num2:
        abs_num1 -= abs_num2


    if num1 < 0:
        return -abs_num1
    else:
        return abs_num1

