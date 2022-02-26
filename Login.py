import settings
import os


print("Welcome to PythonOS!")
print("PythonOS login:")
user_name = input()

if user_name == settings.user:
    print("Enter password:")
    password = input()
    if password == settings.passwd:
        os.system('cls')
        os.system('Shell.py')
    else:
        print("Incorrect password. Close this windows and reopen Login.py")
        input()
else:
    print("Incorrect username. Quit and reopen Login.py")
    input("Press Enter key to quit...")
