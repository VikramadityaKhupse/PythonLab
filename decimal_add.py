def add_decimal(num1, num2):

    num1 = str(num1)
    num2 = str(num2)
    result = ""
    carry = 0
    

    if len(num1) > len(num2):
        num2 = num2.zfill(len(num1))
    elif len(num1) < len(num2):
        num1 = num1.zfill(len(num2))
    

    for i in range(len(num1) - 1, -1, -1):
        addition = int(num1[i]) + int(num2[i]) + carry
        carry = addition // 10
        result += str(addition % 10)
    

    if carry:
        result += str(carry)
    

    return int(result[::-1])
		
	

print(add_decimal(1234, 27))
