import time
import os

print("Please wait, PyOS Installer is installling required packages...")
time.sleep(1)

os.system('pip install --upgrade pip')
os.system('pip install tqdm')
os.system('pip install pathlib')
os.system('pip install requests')


print("Welcome to PyOS Developer Beta 4 Installer!")
print("You will configure the system for your needs.")
print("")
print("Enter username:")

user = input()
f = open("settings.py", "w")
f.write("user = " + '"' + str(user) + '"' + "\n")
f.close()

print("")
print("Enter password (leave blank for none):")

passwd = input()
if passwd == "":
    f = open("settings.py", "a")
    f.write("passwd = " + '""' + "\n")
    f.close()
    print("")
else:
    f = open("settings.py", "a")
    f.write("passwd = " + '"' + str(passwd) + '"' + "\n")
    f.close()

print("")

exec(open("SysCopy.py").read())
