#  https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()
array = input().split()
A = set(input().split())
B = set(input().split())
happiness = 0


for num in array:
    if num in A:
        happiness +=1
    elif num in B:
        happiness += -1
print(happiness)