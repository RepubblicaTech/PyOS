import time, os, json
from System import version

obj = {}

os.system('python -m pip install --upgrade pip')

try:
    import tqdm
except ImportError:
    print("Please wait, " + version.name_full + "Installer is installing required packages...")
    time.sleep(0.5)
    print("")
    print("")
    os.system('pip install tqdm')

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
os.system('cd System && SysCopy.py')
