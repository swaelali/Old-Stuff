def checkio(raw_text):
	queue =[]
	for index in range(len(raw_text)):
		if raw_text[index] in "{[(":
			queue.append(raw_text[index])
		elif raw_text[index] == "}":
			if queue == []:
				return False
			else:
				if queue[-1] != "{":
					return False
				else:
					queue.pop()
		elif raw_text[index] == "]":
			if queue == []:
				return False
			else:
				if queue[-1] != "[":
					return False
				else:
					queue.pop()
		elif raw_text[index] == ")":
			if queue == []:
				return False
			else:
				if queue[-1] != "(":
					return False
				else:
					queue.pop()
	if queue ==[]:
		return True
	else:
		return False
print(checkio("(((1+(1+1))))]"))
	
