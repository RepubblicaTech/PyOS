import settings
import os

print("Welcome to PythonOS!")
print("PythonOS login:")
user_name = input()

if user_name == settings.user:
    print("Enter password:")
    password = input()
    if password == settings.passwd:
        print("Welcome to the Developer Beta 4 of PyOS 0.1!")
        print("Type <help> to see available commands.")
        cwd = input(settings.user + "@pyos # ")
    else:
        print("Incorrect password. Close this windows and reopen OS.py")
        input()
else:
    print("Incorrect username. Quit and reopen OS.py")
    input("Press Enter key to quit...")

if cwd == "update":
    os.system('pip install --upgrade pip')
    os.system('pip install --upgrade tqdm')
    os.system('pip install --upgrade pathlib')
    os.system('pip install --upgrade requests')

if cwd == "print":
    print("Welcome to the Print Shell!")
    input(settings.user + "> ")

if cwd == "help":
    print("3 available commands:")
    print("")
    print("help         See available commands")
    print("print        Works like <echo> in Windows, opens the Print Shell")
    print("update       Checks for updates, still doesn't update OS")

