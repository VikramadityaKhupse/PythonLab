def slice(obj, slicing_param):
    output = [] if isinstance(obj, list) else ""
    step = 1

    if not obj:
        return obj
    if not isinstance(slicing_param, list) or len(slicing_param) > 3:
        return "Slicing param must be [start, end, step]"

    if len(slicing_param) == 1:  # Single index
        return obj[slicing_param[0]]
    elif len(slicing_param) == 2:  # [start, end]
        start, end = slicing_param[0], slicing_param[1]
    elif len(slicing_param) == 3:  # [start, end, step]
        if slicing_param[2] == 0:
            return "Step cannot be zero!!"
        step = slicing_param[2]
        if step > 0:
            start = slicing_param[0] if slicing_param[0] != '-' else 0
            end = slicing_param[1] if slicing_param[1] != '-' else len(obj)
        else:
            start = slicing_param[0] if slicing_param[0] != '-' else len(obj) - 1
            end = slicing_param[1] if slicing_param[1] != '-' else -1

    # Perform slicing
    for i in range(start, end, step):
        if isinstance(output, list):
            output.append(obj[i])
        else:
            output += obj[i]
    
    return output

print(slice([1, 2, 3, 4, 5], ['-', '-', -1]))  
print(slice("abcdef", [1, 2, 1]))             
print(slice("abcdef", [1, 5, 2]))             
print(slice([1, 2, 3, 4, 5], [2, 4]))         
