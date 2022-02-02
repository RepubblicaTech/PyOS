import settings
import os

print("Welcome to PythonOS!")
print("PythonOS login:")
user_name = input()

if user_name == settings.user:
    print("Enter password:")
    password = input()
    if password == settings.passwd:
        print("Welcome!")
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