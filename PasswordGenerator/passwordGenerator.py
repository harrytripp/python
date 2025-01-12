import random
from pathlib import Path

filePath = Path("path/to/file.txt")
minPwdLength = 8
maxPwdLength = 16

while filePath.exists == False:
    print("Invalid path")
    exit()	

content = filePath.read_text().splitlines()
lineTotal = len(content)

password = (''.join(random.sample(content, 3)))
print(password)

if len(password) >= minPwdLength and len(password) <= maxPwdLength:
    print(password)
else:
    pass #TODO reroll password
