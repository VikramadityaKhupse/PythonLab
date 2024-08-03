# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s, r = input().split()
r = int(r)
for i in range(r):
    for j in combinations(sorted(s), i+1):
        print(''.join(j))