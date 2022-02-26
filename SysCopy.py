from tqdm import tqdm
from time import sleep

for i in tqdm(range(100), desc='Copying system files'):
    sleep(0.03)

for i in tqdm(range(100), desc='Installing required packages'):
    sleep(0.05)

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
print("All done! Press Enter to apply changes. Then open Login.py")
input()