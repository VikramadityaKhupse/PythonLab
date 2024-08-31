def base(text, input_base, output_base):
    result = ""
    
    num = int(text, input_base)

    while num > 0:
        digit = num % output_base
        if digit < 10:
            result = str(digit) + result
        else:
            result = chr(ord('A') + digit - 10) + result
        num //= output_base
    return result

        

print(base("E", 16, 10))