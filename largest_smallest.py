def get_set(l):

	temp_set = set()
	
	for obj in l:
		if isinstance(obj, (set, tuple, list)):
		
			temp_set.update(get_set(ibj))
		if isinstance(obj, dict):
			for key in get_set(obj.keys()):
				temp_set.add(key)
			for value in get_set(obj.values()):
				temp_set.add(value)
		elif (isinstance(obj, str) and obj.isdigit()) or isinstance(obj, int):
			temp_set.add(int(obj))
	
	
	return temp_set

def get_sl_ss(l):
	second_smallest, second_largest = 0, 0
	
	
	temp_set = get_set(l)
	
	if len(temp_set) < 3:
		return max(temp_set), min(temp_set)
	
	temp_set.remove(max(temp_set))
	second_largest = max(temp_set)
	temp_set.remove(min(temp_set))
	second_smallest = min(temp_set)
	
	return second_smallest, second_largest
	
test = [{100:300, "strd":900},3, 4, 5, 6, 7, 8, [23, 24, 45, 67, (12, 13, 14, 199, 100)], "123", "0"]
test2 = [10, 20]
print(get_sl_ss(test))
			
