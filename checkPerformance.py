import time

def checkPerformance(approaches):
	time_taken = []
	test = ["aba", "bbb", (1, 2, 22, 121, "bbb", ["bbb", 121]), []]
	for approach in approaches:
		for _ in range(100):
			start_time = time.time()
			approach(test)
			end_time = time.time()
			time_taken.append(end_time-start_time)
	return list(zip(approaches, time_taken))
	
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
		if isinstance(item, str) and len(item)%5 == 3:
			count += ispalindrome(item)
		elif isinstance(item, int):
			item = repr(item)
			if len(item)%5==3:
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
	
def even_odd(l):
	odd_count = 0
	
	for num in l:
		odd_count += num%2
		
	return odd_count, len(l)-odd_count
	
test = [(1, 2, 22, 121, "bbb", ["bbb", 121]), [], "aba", "bbb",]
test2 = [1, 2, 3, 4, 5, 6, 7]
print(even_odd(test2))
print(f"Approach 1: {approach1(test)}")
print(f"Approach 2: {approach2(test)}")
print(f"Approach 2: {approach3(test)}")
print(checkPerformance([approach1, approach2, approach3]))

