def change_case(text, style):
    styles = ('s', 'c', 'r', 'z')

    if not style.casefold() in styles:
        print(
            "Please enter appropriate style option i.e.\n1) s for small\n2) c for capital\n3) r for reversed\n4) z for zigzag")
    else:
        if style.casefold() == 's':
            return small(text)
        elif style.casefold() == 'c':
            return capital(text)
        elif style.casefold() == 'r':
            return reverse(text)
        elif style.casefold() == 'z':
            return zigzag(text)


def capital(text):
    result = ""
    for index, char in enumerate(text):
        if index == 0 and 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif index != 0 and 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char

    return result


def small(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result


def reverse(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result


def zigzag(text):
    result = ""
    if 'A' <= text[0] <= 'Z':
        for index, char in enumerate(text):
            if index % 2 == 0 and 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            elif index % 2 != 0 and 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
    if 'a' <= text[0] <= 'z':
        for index, char in enumerate(text):
            if index % 2 == 0 and 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            elif index % 2 != 0 and 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
    return result


print(change_case("I am VIKRAMDITYa", 'c'))
print(change_case("I am VIKRAMDITYa", 's'))
print(change_case("I am VIKRAMDITYa", 'r'))
print(change_case("Vikram", 'z'))
