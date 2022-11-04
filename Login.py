import os, json
from System import version

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
        os.system('cls')
        os.system('cd System && Shell.py')
    else:
        print("Incorrect password. Close this windows and reopen Login.py")
        input()
else:
    print("Incorrect username. Quit and reopen Login.py")
    input("Press Enter key to quit...")