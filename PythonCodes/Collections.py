# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N  = int(input())
names = input().split()
position: int = names.index('MARKS')
sum = 0
for _ in range(N):
    student_data = input().split()
    sum += int(student_data[position])
print(round((sum/N), 2))
    
    