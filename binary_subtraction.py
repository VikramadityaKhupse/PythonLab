def binary_subtraction(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    
    result = ''
    borrow = 0
    
    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        
        sub = bit1 - bit2 - borrow
        
        if sub == -1:
            borrow = 1
            result = '1' + result
        elif sub == -2:
            borrow = 1
            result = '0' + result
        else:
            borrow = 0
            result = str(sub) + result
    
    return result.lstrip('0') or '0'


print(binary_subtraction('1011', '1001'))