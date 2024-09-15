def binary_char_to_int(char: str) -> int:
    if char == '0':
        return 0
    elif char == '1':
        return 1
    else:
        raise ValueError(f"Invalid binary character: {char}")

def binary_addition(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    
    result = ''
    carry = 0
    
    for i in range(max_len - 1, -1, -1):
        bit1 = binary_char_to_int(bin1[i])
        bit2 = binary_char_to_int(bin2[i])
        
        sum_bits = bit1 + bit2 + carry
        
        if sum_bits == 2:  
            result = '0' + result
            carry = 1
        elif sum_bits == 3:  
            result = '1' + result
            carry = 1
        else:
            result = str(sum_bits) + result
            carry = 0
    
    if carry:
        result = '1' + result
    
    return result.lstrip('0') or '0'

print(binary_addition('1011', '1001')) 
