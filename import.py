#!/usr/bin/python2.7

# Extract from Python CGI project

QUERY_STRING = "email=rob%40test.com&username=rob&password=password&hostname=hostname&protocolin=IMAP&ssl=True"	
L = {}

# Convert query_string in to a dictionary 
if QUERY_STRING != "":
	X = 0
	QUERY_LIST = QUERY_STRING.split('&')
	QUERY_LEN = len(QUERY_LIST)
	
	while X < QUERY_LEN:
		if "email" in QUERY_LIST[X] :
			QUERY_LIST[X] = QUERY_LIST[X].replace("%40", "@")
		TMP = QUERY_LIST[X].split('=')
		L[TMP[0]] = TMP[1]
		X = X + 1
	if 'portin' in L:
		L['portin']
	else:
		if L['protocolin'] == "IMAP":
			if L['ssl'] != "True":
				L['portin'] = 143
			else:
				L['portin'] = 993
		if L['protocolin'] == "POP3":
			if L['ssl'] != "True":
				L['portin'] = 110
			else:
				L['portin'] = 995
	if 'portout' in L:
		L['portout']
	else:
		if L['ssl'] != "True":
			L['portout'] = 25
		else:
			L['portout'] = 465
	
print L


# Open text.txt and replace the placement variables
with open('text.txt', 'r') as inputfile:
	template = inputfile.read()
	template = template.replace("[[EMAIL]]", L['email'])
	template = template.replace("[[USER]]", L['username'])
	template = template.replace("[[PASS]]", L['password'])
	template = template.replace("[[HOST]]", L['hostname'])
	# Expecting string to replace with
	template = template.replace("[[PORTIN]]", str(L['portin']))
	template = template.replace("[[PORTOUT]]", str(L['portout']))
	print template






