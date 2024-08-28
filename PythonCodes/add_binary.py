# https://leetcode.com/problems/add-binary/
a = "11"
b ="1"
bin_1 = bin(int("0b"+a, 2) & int("0b"+b, 2))
print(bin_1)