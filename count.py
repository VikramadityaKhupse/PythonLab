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

print(count("gggggg", "gg", not True))
def count2(string, s, overlapping):
	pass



# OPTIMIZED VERSION:
# def count(string, s, overlapping):
#     output = 0
#     s_len = len(s)

#     if overlapping:
#         i = 0
#         while i <= len(string) - s_len:
#             if string[i:i + s_len] == s:
#                 output += 1
#             i += 1
#     else:
#         i = 0
#         while i <= len(string) - s_len:
#             if string[i:i + s_len] == s:
#                 output += 1
#             i += s_len

#     return output


# print(count("gggggg", "gg", True))

# (base) vikramaditya@vikramaditya-Victus:~/Desktop/Python$ time vikram count.py (non-optmized)
# 5

# real	0m0.014s
# user	0m0.014s
# sys	0m0.000s
0

# (base) vikramaditya@vikramaditya-Victus:~/Desktop/Python$ time vikram count.py (non-optmized)
# 5

# real	0m0.011s
# user	0m0.007s
# sys	0m0.003s
