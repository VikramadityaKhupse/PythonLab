# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    try:
        command = input().split()
        if command[0] == "pop":
            s.pop()
        elif command[0] == "remove":
            s.remove(int(command[1]))
        elif command[0] == "discard":
            s.discard(int(command[1]))
    except KeyError:
        continue

print(sum(s))