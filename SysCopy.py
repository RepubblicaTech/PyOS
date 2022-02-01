from tqdm import tqdm
from time import sleep
import settings

for i in tqdm(range(100), desc='Copying system files'):
    sleep(0.03)

for i in tqdm(range(100), desc='Installing required packages'):
    sleep(0.05)

for i in tqdm(range(100), desc='Installing patches'):
    sleep(0.003)

for i in tqdm(range(100), desc='Setting up environment'):
    sleep(0.03)

for i in tqdm(range(100), desc='Setting up directory tree'):
    sleep(0.02)

f = open("settings.py", "a")
f.write("%s \n %s \n" % ("root = " + '"/"', "home = " + '"/" + user'))

for i in tqdm(range(100), desc='Setting up user'):
    sleep(0.02)

print("")
print("All done! Close this window and open OS.py")
input()