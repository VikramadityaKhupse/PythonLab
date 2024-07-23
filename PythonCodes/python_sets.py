# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
# Read the number of elements in the set
n = int(input())

# Read the elements of the set
s = set(map(int, input().split()))

# Read the number of commands
m = int(input())

# Execute each command
for _ in range(m):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

# Print the sum of the remaining elements in the set
print(sum(s))