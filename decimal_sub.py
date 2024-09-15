def string_to_int(s: str) -> int:
    result = 0
    is_negative = False

    if not s:
        raise ValueError("Empty string cannot be converted to integer")

    if s[0] == '-':
        is_negative = True
        s = s[1:]

    for char in s:
        if char < '0' or char > '9':  
            raise ValueError(f"Invalid character '{char}' in input string")
        result = result * 10 + (ord(char) - ord('0'))

    if is_negative:
        result = -result

    return result


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
        subtraction = string_to_int(num1[i]) - string_to_int(num2[i]) - borrow
        if subtraction < 0:
            subtraction += 10
            borrow = 1
        else:
            borrow = 0
        result += str(subtraction)

    result = result.rstrip('0')

    if not result:
        return 0

    return string_to_int(result[::-1])  


print(subtract_decimal(2000, 999))  
