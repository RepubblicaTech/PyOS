import time
import os

print("Please wait, PyOS Installer is installing required packages...")
time.sleep(0.5)
print("")
print("")

os.system('pip install --upgrade pip')
os.system('pip install tqdm')
os.system('pip install requests')
os.system('pip install pywin32 --upgrade')
os.system('pip install keyboard')
time.sleep(0.3)
os.system('cls')

print("Welcome to PyOS v0.1.3 Post-Reset Installer!")
print("You will configure the system for your needs.")
print("")
print("Enter username:")

user = input()
f = open("System\settings.py", "w")
f.write("user = " + '"' + str(user) + '"' + "\n")
f.close()

print("")
print("Enter password (leave blank for none):")

passwd = input()
if passwd == "":
    f = open("System\settings.py", "a")
    f.write("passwd = " + '""' + "\n")
    f.close()
    print("")
else:
    f = open("System\settings.py", "a")
    f.write("passwd = " + '"' + str(passwd) + '"' + "\n")
    f.close()

print("")

exec(open("SysCopy.py").read())
