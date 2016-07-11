def rot(str, num, codify):
	result = ""
	for s in str:
		if ord(s) is not 32: # verification on blank symbol
			s = transform_char(s, num, codify)
			result += s
		else:
			result += " "
	return result	

# codify/uncodify one character
def transform_char(char, num, codify):
	char_to_int = ord(char)
	# codify
	num %= 26 
	if codify:
		print("Codify = True")
		result_char = char_to_int + num	
	# uncodify	
	else:
		print("Codify = False")
		result_char = char_to_int - num	
	result_char = char_to_int + num	
	# lower case 
	if char_to_int > 96 and char_to_int < 123:
		if  result_char > 122:
			result_char = result_char - 122 + 96
		if result_char < 97:
			result_char = 123 - (97 - result_char)
	# upper case			
	if char_to_int > 64 and char_to_int < 91:
		if  result_char > 90:
			result_char = result_char - 90 + 64
		if result_char < 65:
			result_char = 91 - (65 - result_char)	
	return chr(result_char)	


string = "z"
codify = False
print(rot(string, -1, codify))
