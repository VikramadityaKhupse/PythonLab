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
        addition = string_to_int(num1[i]) + string_to_int(num2[i]) + carry
        carry = addition // 10
        result += str(addition % 10)

    if carry:
        result += str(carry)

    return string_to_int(result[::-1])  


print(add_decimal(1234, 27))  
