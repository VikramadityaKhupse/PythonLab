# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = set()
for _ in range(int(input())):
    s.add(input())

print(len(s))