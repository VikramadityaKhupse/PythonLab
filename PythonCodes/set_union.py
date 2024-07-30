# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
E = int(input())
E_students = set(input().split())
F = int(input())
F_students = set(input().split())
print(len(E_students.union(F_students)))


    
    
    