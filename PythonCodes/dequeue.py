# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()


for _ in range(int(input())):
    command = input().split()
    if len(command)>1:
        num = command[1]
    command = command[0]
    if command == "append":
        d.append(num)
    elif command == "appendleft":
        d.appendleft(num)
    elif command == "pop":
        d.pop()
    elif command == "popleft":
        d.popleft()

print(' '.join(d))
    
    
    
    
# OPTIMIZED

# from collections import deque
# import sys

# input = sys.stdin.read
# data = input().splitlines()

# d = deque()

# commands = {
#     "append": d.append,
#     "appendleft": d.appendleft,
#     "pop": d.pop,
#     "popleft": d.popleft
# }

# for line in data[1:]:
#     command, *args = line.split()
#     if args:
#         commands[command](args[0])
#     else:
#         commands[command]()

# print(" ".join(d))

