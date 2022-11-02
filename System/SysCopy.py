from tqdm import tqdm
from time import sleep

for i in tqdm(range(100), desc='Copying system files'):
    sleep(0.03)
for i in tqdm(range(100), desc='Seeting up user environment'):
    sleep(0.03)

print("")
print("All done! Press Enter to apply changes. Then open Login.py")
input()
