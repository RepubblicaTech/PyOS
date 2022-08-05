from ensurepip import version
import os
from System import user,version

print("Welcome to " + version.name_full + version.about + "!")
print("PythonOS login:")
user_name = input()

if user_name == user.user:
    print("")
    print("Enter password:")
    password = input()
    if password == user.passwd:
        os.system('cls')
        os.system('cd System && Shell.py')
    else:
        print("Incorrect password. Close this windows and reopen Login.py")
        input()
else:
    print("Incorrect username. Quit and reopen Login.py")
    input("Press Enter key to quit...")
