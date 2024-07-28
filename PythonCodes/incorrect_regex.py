# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for i in range(T):
    p = input().strip()
    try:
        re.compile(p)
        print(True)
    except re.error:
        print(False)
    
