def isIdentifier(string):
	if not string:
		return False
	elif string[0].isdigit():
		return False
	elif " "  in string:
		return False
	else:
		return True


s = "____abcd00"
print(s.isidentifier())
print(isIdentifier(s))
	
