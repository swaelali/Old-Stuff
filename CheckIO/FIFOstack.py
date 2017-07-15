def letter_queue(commandlist):
	stack=[]
	stacktext=""
	for index in range(len(commandlist)):
		command = commandlist[index]
		if "PUSH" in command:
			stack.append(command[-1])
		elif "POP" in command:
			if stack != []:
				stack.remove(stack[0])
	for i in range(len(stack)):
		stacktext = stacktext + stack[i]
	return stacktext
print letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"])
print letter_queue(["POP", "POP"])
print letter_queue(["PUSH H", "PUSH I"])
print letter_queue([])
