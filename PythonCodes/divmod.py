# https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b, = int(input()), int(input())
print(a // b)
print(a%b)
print(divmod(a, b))