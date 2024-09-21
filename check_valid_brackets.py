def check_validity(text: str) -> str:
    bracket_pairs = {
        ')': '(', 
        ']': '[', 
        '}': '{', 
        '>': '<'
    }
    
    stack = []
    
    for index, char in enumerate(text):
        if char in bracket_pairs.values(): 
            stack.append(char)
        elif char in bracket_pairs:  
            if not stack:
                return f"Invalid: Closing bracket '{char}' at position {index} has no matching opening."
            if stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                return f"Invalid: Bracket '{char}' at position {index} mismatched with '{stack[-1]}'."
        elif char not in '[]{}()<>' and char.isalnum():
            continue  
        else:
            return f"Invalid: Character '{char}' at position {index} is not a valid bracket."
    
    if stack:
        return f"Invalid: Unbalanced opening bracket(s) remaining: {stack}."
    
    return "valid"

def get_valid_invalid_text_count(texts: list) -> tuple:
    valid_count = 0
    invalid_count = 0
    
    for item in texts:
        if isinstance(item, str): 
            result = check_validity(item)
            if result == "valid":
                valid_count += 1
            else:
                invalid_count += 1
                print(f"Invalid text '{item}': {result}")
        else:
            invalid_count += 1
    
    return valid_count, invalid_count


texts = ['[{(', [45, ("()"), ]]
print(get_valid_invalid_text_count(texts))

