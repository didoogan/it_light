def rot(str, num, reverse=True):
	#to_num = None
	# to_char = ''
	result = ""
	for s in str:
		if ord(s) is not 32:
			s = transform_char(s, num, reverse=reverse)
			result += s
		else:
			result += " "
	return result	


def transform_char(char, num, reverse=True):
	num %= 26
	if reverse:
		char_to_int = ord(char) + num
	else:
		char_to_int = ord(char) - num	
	# deal with Capitalize char
	if char_to_int > 90 and char_to_int < 97: 
		if char_to_int > 90 and char_to_int < 97:
			char_to_int = char_to_int - 90 + 64
	# deal with lowercase char		
	else: 	
		if  char_to_int  > 122:
			char_to_int = char_to_int - 122 + 96
	return chr(char_to_int)


string = 'BBBb b'
#print(transform_char(string, 1))
print(rot(string, 555555555555555))











