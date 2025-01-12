import random
from pathlib import Path

filePath = Path("/home/harry/Dev/Python/PasswordGenerator/Sources/words.txt")

if filePath.exists():
    pass
else:
	print("Invalid path")
	exit()

with filePath.open() as file:
	for count, line in enumerate(file):
		lineTotal = (count + 1)
		pass

with filePath.open() as file:
    content = file.readlines()

print(content[random.randint(0, int(lineTotal))])
