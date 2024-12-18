import time


def checkPerformance(approaches):
    time_taken = []
    # test = [1, 2, 3, 4, 5, 6, 7]
    test = [(1, 2, 22, 121, "bbb", ["bbb", 121]), [], "aba", "bbb",]

    for approach in approaches:
        start_time = time.time()
        for _ in range(100000):
            approach(test)
        end_time = time.time()
        time_taken.append(end_time - start_time)

    first_approach_time = time_taken[0]
    percentage_faster = []
    
    for i in range(1, len(approaches)):
        percentage_diff = ((first_approach_time - time_taken[i]) / first_approach_time) * 100
        percentage_faster.append((approaches[i].__name__, percentage_diff))
    
    return time_taken, percentage_faster


#____________________________________________________________________________________
def approach1(l):
    count = 0
    if not l:
        return 0
    for item in l:
        if type(item) in (list, tuple, set):
            count += approach1(item)
        else:
            item = str(item)
            if (len(item) % 5 == 3) and (item == item[::-1]):
                count += 1
    return count


def ispalindrome(item):
    return item == item[::-1]


def approach2(l):
    count = 0
    for item in l:
        if isinstance(item, str) and len(item) % 5 == 3:
            count += ispalindrome(item)
        elif isinstance(item, int):
            item = repr(item)
            if len(item) % 5 == 3:
                count += ispalindrome(item)
        elif isinstance(item, (list, tuple, set)):
            count += approach2(item)
    return count


def approach3(objects):
    count = 0
    for obj in objects:
        if isinstance(obj, (list, tuple, set)):
            count += approach3(obj)
        elif isinstance(obj, int):
            obj = str(obj)
        count += isinstance(obj, str) and len(obj) % 5 == 3 and ispalindrome(obj)
    return count

    # ___________________________________________________________________________


def odd_even1(l):
    odd_count = 0

    for num in l:
        odd_count += num % 2

    return odd_count, len(l) - odd_count


def odd_even2(l):
    odd_count = 0

    for num in l:
        if num % 2 != 0:
            odd_count += 1

    return odd_count, len(l) - odd_count


# test = [(1, 2, 22, 121, "bbb", ["bbb", 121]), [], "aba", "bbb",]
test2 = [1, 2, 3, 4, 5, 6, 7]
# print(odd_even1(test2))
# print(odd_even2(test2))

# print(f"Approach 1: {approach1(test)}")
# print(f"Approach 2: {approach2(test)}")
# print(f"Approach 2: {approach3(test)}")
time_taken, percentage_faster = checkPerformance([approach1, approach2,approach3])
print("Execution times (in seconds):", time_taken)
print("Percentage faster than the first approach:", percentage_faster)