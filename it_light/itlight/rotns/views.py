from django.shortcuts import render
from django import forms
from django.http import HttpResponse

class RotnForm(forms.Form):
	input = forms.CharField(widget=forms.Textarea)
	number = forms.IntegerField(required=True)

def index(request):
	if request.method == 'POST':
		form = RotnForm(request.POST)
		if form.is_valid():
			input = form.cleaned_data['input']
			number = form.cleaned_data['number']
		if 'codify' in request.POST and form.is_valid:
			result = rot(input, number)
		elif 'uncodify' in request.POST and form.is_valid:
			result = rot(input, number, False)
		return render(request, 'index.html', {"form": form, "result": result})
	else:
		form = RotnForm()	
	return render(request, 'index.html', {"form": form})

def rot(str, num, codify=True):
	#to_num = None
	# to_char = ''
	result = ""
	for s in str:
		if ord(s) is not 32:
			s = transform_char(s, num, codify=codify)
			result += s
		else:
			result += " "
	return result	


def transform_char(char, num, codify=True):
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


