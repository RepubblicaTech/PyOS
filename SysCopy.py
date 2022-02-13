from tqdm import tqdm
from time import sleep
from pathlib import Path

for i in tqdm(range(100), desc='Copying system files'):
    sleep(0.03)

for i in tqdm(range(100), desc='Installing user-friendly'):
    sleep(0.05)

history = Path("manual.py")

if history.is_file():
    txt = open("tutorial.txt", "w")
    txt.write("This a sample text file.")
    txt.write("Do not edit it or delete it.")
else:
    path = open("tutorial.txt", "x")
    path.close()
    txt = open("tutorial.txt", "w")
    txt.write("This a sample text file. ")
    txt.write("Do not edit it or delete it.")

for i in tqdm(range(100), desc='Installing patches'):
    sleep(0.003)

for i in tqdm(range(100), desc='Setting up environment'):
    sleep(0.03)

for i in tqdm(range(100), desc='Setting up directory tree'):
    sleep(0.02)

f = open("settings.py", "a")
f.write("root = " + '"/"' + "\n")
f.write("home = " + '"/" + user' + "\n")

for i in tqdm(range(100), desc='Setting up user'):
    sleep(0.02)

print("")
print("All done! Press Enter to close this window and open OS.py")
input()