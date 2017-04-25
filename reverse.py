#Custom way
def reverse_string(text):
	if len(text) < 1:
		return text

	return reverse_string(text[1:]) + text[0]


mystring = reverse_string('hello')

print(mystring)

#Standard way
mystring2 = 'helloworld'
print(mystring2[::-1])

