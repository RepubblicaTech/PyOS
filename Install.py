import time, os, platform
from System import version

plt = platform.system()

time.sleep(1)

if plt == "Linux":
    os.system('clear')
elif plt == "Windows":
    os.system('cls')

for i in range(3):
    print("Checking system compatibility")
    time.sleep(0.5)
    if plt == "Linux":
        os.system('clear')
    elif plt == "Windows":
        os.system('cls')
    print("Checking system compatibility.")
    time.sleep(0.5)
    if plt == "Linux":
        os.system('clear')
    elif plt == "Windows":
        os.system('cls')
    print("Checking system compatibility..")
    time.sleep(0.5)
    if plt == "Linux":
        os.system('clear')
    elif plt == "Windows":
        os.system('cls')
    print("Checking system compatibility...")
    time.sleep(0.5)
    if plt == "Linux":
        os.system('clear')
    elif plt == "Windows":
        os.system('cls')

if plt == "Linux":
    print("Error 0x01: Sorry, Linux system are not supported.")
    print("If you want to add Linux compatibility, fork the project from GitHub Repo:")
    print("https://github.com/RepubblicaTech/PyOS")
    time.sleep(5)
    exit(0)

print("Please wait, " + version.name + "Installer is installing required packages...")
time.sleep(0.5)
print("")
print("")

os.system('python -m pip install --upgrade pip')
os.system('pip install tqdm')
time.sleep(0.3)
os.system('cls')

print("Welcome to " + version.name + version.about + " Installer!")
print("You will configure the system for your needs.")
print("")
print("Enter username:")

user = input()
f = open("System/user.py", "w")
f.write("user = " + '"' + str(user) + '"' + "\n")
f.close()

print("")
print("Enter password (leave blank for none):")

passwd = input()
if passwd == "":
    f = open("System/user.py", "a")
    f.write("passwd = " + '""' + "\n")
    f.close()
    print("")
else:
    f = open("System/user.py", "a")
    f.write("passwd = " + '"' + str(passwd) + '"' + "\n")
    f.close()

print("")
os.system('cd System && SysCopy.py')
