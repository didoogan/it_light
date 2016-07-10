def transfortm_char(char, num, codify=True):
	result = None
	result_char = None
	char_to_int = ord(char)
	# codify 
	if codify:
		num %= 26
	else:
	# uncodify	
		num %= 26
		num *= -1
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


print(transfortm_char('D', 5))