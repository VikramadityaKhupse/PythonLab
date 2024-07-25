# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
ordered_dict = OrderedDict()
N = int(input())
s =[]
for _ in range(N):
    s.append(input().strip())
for word in s:
    if word in ordered_dict:
        ordered_dict[word] += 1
    else:
        ordered_dict[word] = 1
        
print(len(ordered_dict))
print(' '.join(map(str, ordered_dict.values())))
    