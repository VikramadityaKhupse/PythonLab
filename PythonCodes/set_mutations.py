# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
# Reading input
num_elements_A = int(input())
A = set(map(int, input().split()))

n = int(input())

# Processing each operation
for _ in range(n):
    operation, _ = input().split()
    other_set = set(map(int, input().split()))
    
    # Perform the corresponding operation on set A
    if operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "update":
        A.update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)

# Output the sum of elements in set A
print(sum(A))
