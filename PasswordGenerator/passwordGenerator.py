import random

filePath = "path/to/file.txt"

file = open(filePath)
content = file.readlines() 

with open(filePath, 'r') as file:
	for count, line in enumerate(file):
		pass
lineTotal = (count + 1)

print(content[random.randint(0, int(lineTotal))])
