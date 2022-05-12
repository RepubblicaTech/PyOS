import os

from System import settings

print("Welcome to PythonOS v0.1.3 Post-Reset Beta 1!")
print("PythonOS login:")
user_name = input()

if user_name == settings.user:
    print("")
    print("Enter password:")
    password = input()
    if password == settings.passwd:
        os.system('cls')
        os.system('System\Shell.py')
    else:
        print("Incorrect password. Close this windows and reopen Login.py")
        input()
else:
    print("Incorrect username. Quit and reopen Login.py")
    input("Press Enter key to quit...")
