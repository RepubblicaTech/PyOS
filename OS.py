import settings
from settings import user
import os

print("Welcome to PythonOS!")
print("PythonOS login:")
user_name = input()

if user_name == user:
    print("Enter password:")
    password = input()
    if password == settings.passwd:
        print("Welcome to the Developer Beta 3 of PyOS 0.1!")
        print("Type <start> (the only command available) to open the Start Guide!")
        cwd = input(settings.user + "@pyos # ")
    else:
        print("Incorrect password. Close this windows and reopen OS.py")
        input()
else:
    print("Incorrect username. Quit and reopen OS.py")
    input("Press Enter key to quit...")

if cwd == "start":
    os.system('cls')
    os.system('Guide.py')

if cwd == "print":
    print("Welcome to the Print Shell!")
    input(settings.user + "> ")