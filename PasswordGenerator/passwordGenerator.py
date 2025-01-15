import random
from pathlib import Path

filePath = Path("path/to/file.txt")
minPwdLength = 15
maxPwdLength = 15
minStrLengh = 4

while filePath.exists == False:
    print("Invalid path")
    exit()	

contentRaw = filePath.read_text().splitlines()
content = [line for line in contentRaw if len(line) != minStrLengh]
lineTotal = len(content)
def getSymbol():
    symbols = ['!', '@', '#', '$', '%', '*', '?', '-', '_', '.']
    return random.choice(symbols)

def genComplex():
    #password = ''.join(word.capitalize() for word in random.sample(content, 3))
    password = f'{getSymbol()}'.join(word.capitalize() for word in random.sample(content, 3))

    if len(password) >= minPwdLength and len(password) <= maxPwdLength:
        print(password)
    else:
        genComplex()

def generate():
    password = (''.join(random.sample(content, 3)))

    if len(password) >= minPwdLength and len(password) <= maxPwdLength:
        print(password)
    else:
        generate()

genComplex()
