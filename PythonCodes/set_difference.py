# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
E,S = int(input()), input().split()
F,S2 = int(input()), input().split()

print(len(set(S).difference(set(S2))))