import time, os
from System import version

print("Please wait, " + version.name_full + "Installer is installing required packages...")
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
