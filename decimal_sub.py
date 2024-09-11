def subtract_decimal(num1, num2):

    num1 = str(num1)
    num2 = str(num2)
    result = ""
    borrow = 0
    

    if len(num1) > len(num2):
        num2 = num2.zfill(len(num1))
    elif len(num1) < len(num2):
        num1 = num1.zfill(len(num2))
    

    for i in range(len(num1) - 1, -1, -1):
        subtraction = int(num1[i]) - int(num2[i]) - borrow
        if subtraction < 0:
            subtraction += 10
            borrow = 1
        else:
            borrow = 0
        result += str(subtraction)
    

    result = result.rstrip('0')
    

    if not result:
        return 0
    

    return int(result[::-1])
    
print(subtract_decimal(2000, 999))
