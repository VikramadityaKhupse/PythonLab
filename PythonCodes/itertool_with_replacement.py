# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s, k = input().split()
k = int(k)

for char in combinations_with_replacement(sorted(s), k):
    print(''.join(char))