import time, os
from sys import platform
from System import version

plt = platform

time.sleep(1)

if plt == "linux" or plt == "linux2":
    os.system('clear')
elif plt == "win32":
    os.system('cls')

for i in range(3):
    print("Checking system compatibility")
    time.sleep(0.5)
    if plt == "linux" or plt == "linux2":
        os.system('clear')
    elif plt == "win32":
        os.system('cls')
    print("Checking system compatibility.")
    time.sleep(0.5)
    if plt == "linux" or plt == "linux2":
        os.system('clear')
    elif plt == "win32":
        os.system('cls')
    print("Checking system compatibility..")
    time.sleep(0.5)
    if plt == "linux" or plt == "linux2":
        os.system('clear')
    elif plt == "win32":
        os.system('cls')
    print("Checking system compatibility...")
    time.sleep(0.5)
    if plt == "linux" or plt == "linux2":
        os.system('clear')
    elif plt == "win32":
        os.system('cls')

if plt == "linux" or plt == "linux2":
    print("Error 0x01: Sorry, Linux system are not supported.")
    print("If you want to add Linux compatibility, fork the project from GitHub Repo:")
    print("https://github.com/RepubblicaTech/PyOS")
    time.sleep(5)
    exit(0)
elif plt == "darwin":
    print("WARNING!")
    print("As i don't have a macOS / OS X system, i don't know if PyOS works on this system.")
    print("You can report bugs in the Issues section of the repo.")
    print("If you know what are you doing, press Enter to continue...")
    input()
elif plt == "win32":
    print("OK! You're good to go.")
    time.sleep(3)
    os.system('cls')

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
