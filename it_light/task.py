def transform_char(char, num):
	char_to_int = None
	char_to_int = ord(char) + num
	# deal with Capitalize char
	if char_to_int > 90 and char_to_int < 97: 
		if char_to_int > 90 and char_to_int < 97:
			char_to_int = char_to_int - 90 + 64
	# deal with lowercase char		
	else: 	
		if  char_to_int  > 122:
			char_to_int = char_to_int - 122 + 96
	return char_to_int



	
print(chr(transform_char('z', 6)))	


	