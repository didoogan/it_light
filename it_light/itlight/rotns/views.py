import os
from django.shortcuts import render
from django import forms
from django.http import HttpResponse, JsonResponse



class RotnForm(forms.Form):
	input = forms.CharField(widget=forms.Textarea(attrs={
		'id': 'post-text',
		'placeholder': 'Input text',
	}), label='')
	num = forms.IntegerField(initial=777)
	output = forms.CharField(widget=forms.Textarea(attrs={'id': 'result-text', 'disabled': True}), label='')

	
def index(request):
	if request.method == 'POST':
		json = {}
		input, json['input'] = (request.POST.get('the_post'),) *2
		number,json['number'] = (int(request.POST.get('the_number')),) *2
		codify, json['codify'] = (request.POST.get('codify'),) *2
		json['result'] = rot(input, number, codify)
		json['chart'] = frequency_of_chars(input)
		json['suggest'] = is_english_word(input)
		print is_english_word(input)
		return JsonResponse(json)
	else:
		form = RotnForm()
		return render(request, 'index.html', {"form": form})

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
	if codify == 'True':
		result_char = char_to_int + num	
	# uncodify	
	else:
		result_char = char_to_int - num	
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

def frequency_of_chars(str):
	result = {}
	for s in str:
		if s == " ":
			continue
		if s in result:
			result[s] = result[s] + 1
		else:	
			result[s] = 1
	return result	

def is_english_word(str):
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'words.txt')
	# file = static("../static/css/bootstrap.css")
	with open(file_path) as word_file:
		english_words = set(word.strip().lower() for word in word_file)
	arr = str.strip().split(' ')
	for i in range(0,26):
		for string in arr:
			if rot(string.lower(), i, True) in english_words:
				return "For uncodifying string, you should take {} steps and press 'codify'".format(26-i)
	return 'No suggest'	



