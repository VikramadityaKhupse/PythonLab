def count(string, s, overlapping):
    output = 0
    s_len = len(s)
    if overlapping:
        rng = len(string) + 1 - s_len
        for i in range(rng):
            if string[i:s_len] == s:
                output += 1
            s_len += 1
    else:
        rng = len(string) // s_len
        j = 0
        k = s_len
        for i in range(rng):
            if string[j:k] == s:
                output += 1
            j += s_len
            k += s_len

    return output


print(count("gggggg", "gg", True))



