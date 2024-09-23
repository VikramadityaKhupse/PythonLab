def isIdentifier(string):
	if not string or string[0].isdigit() or " "  in string  :
		return False
	else:
		return True


s = "____abcd00"
print(s.isidentifier())
print(isIdentifier(s))
	
