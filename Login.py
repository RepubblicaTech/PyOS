import os, json, sys
from System import version

system = sys.platform

print("Welcome to " + version.name_full + version.about + "!")
print("PythonOS login:")
user_name = input()

global username, passwd
username = ""
passwd = ""

pyos_env = json.load(open("System/user.json"))

for pyos in pyos_env['PyOS_Env']:
    username = pyos["Username"]
    passwd = pyos["Password"]

if user_name == username:
    print("")
    print("Enter password:")
    password = input()
    if password == passwd:
        if system == "win32" or system == "darwin":
            os.system('cls')
            os.system('cd System && Shell.py')
        elif system == "linux":
            os.system('clear')
            os.system('cd System && python3 Shell.py')
    else:
        print("Incorrect password. Close this windows and reopen Login.py")
        input()
else:
    print("Incorrect username. Quit and reopen Login.py")
    input("Press Enter key to quit...")