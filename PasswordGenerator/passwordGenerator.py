import random
from pathlib import Path

filePath = Path("path/to/file.txt")

while filePath.exists == False:
    print("Invalid path")
    exit()	

content = filePath.read_text().splitlines()
lineTotal = len(content)

print(content[random.randint(0, int(lineTotal))])
