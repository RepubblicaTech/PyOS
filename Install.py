import time, os, json, platform
from System import version

obj = {}

print("Please wait, " + version.name_full + "Installer is installing required packages...")
time.sleep(0.5)
print("")
print("")

if(platform.platform().__contains__("windows".lower())):
    os.system('python -m pip install --upgrade pip')
    os.system('pip install tqdm')
    time.sleep(0.3)
    os.system('cls')
else:
    os.system('python3 -m pip install --upgrade pip')
    os.system('pip3 install tqdm')
    time.sleep(0.3)
    os.system('cls')

print("Welcome to " + version.name + version.about + " Installer!")
print("You will configure the system for your needs.")
print("")
print("Enter username:")

user = input()

print("")
print("Enter password (leave blank for none):")

passwd = input()

obj["PyOS_Env"] = [{"Username" : user, "Password" : passwd}]
pyos_json = open("System/user.json", "w")

json.dump(obj, pyos_json)

print("")

if(platform.platform().__contains__("windows".lower())):
    os.system('cd System && SysCopy.py')
else:
    os.system('cd System && python3 SysCopy.py')
