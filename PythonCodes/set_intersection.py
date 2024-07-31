# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
E = int(input())
set1 = set(input().split())
F = int(input())
set2 = set(input().split())
print(len(set1.intersection(set2)))