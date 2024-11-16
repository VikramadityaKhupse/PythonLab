def to_roman(value):
    roman_map = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
        90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX",
        5: "V", 4: "IV", 1: "I"
    }
    
    roman_keys = sorted(roman_map.keys(), reverse=True)

    if isinstance(value, str):
        if value.startswith("0b"):
            value = int(value, 2)
        elif value.startswith("0x"):
            value = int(value, 16)
        elif value.startswith("0o"):
            value = int(value, 8)
        else:
            value = int(value) 

    result = ""
    for key in roman_keys:
        while value >= key:
            result += roman_map[key]
            value -= key

    return result

print(to_roman("0xddd"))  
