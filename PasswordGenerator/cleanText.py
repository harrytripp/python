from pathlib import Path

filePath = Path("/home/harry/Dev/Python/PasswordGenerator/Sources/words.txt")

while filePath.exists == False:
    print("Invalid path")
    exit()	

content = filePath.read_text().splitlines()
lineTotal = len(content)
clean = [i.split(' ', 1)[0] for i in content]