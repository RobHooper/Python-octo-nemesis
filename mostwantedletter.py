#!/usr/bin/python2.7

def checkio(text):

	print(text)

#	string = string.replace(" ","")
#	list = []
#	for char in string:
#		list.append(char)
#		
#	dict['t'] = '3'
#	
#	return 'a'


checkio(u"Hello World!") == "l", "Hello test"
checkio(u"How do you do?") == "o", "O is most wanted"
checkio(u"One") == "e", "All letter only once."
checkio(u"Oops!") == "o", "Don't forget about lower case."
checkio(u"AAaooo!!!!") == "a", "Only letters."
checkio(u"abe") == "a", "The First."
#print("Start the long test")
#checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
print("The local tests are done.")

