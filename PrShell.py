import settings
import os

print("Welcome to the Print Shell!")
print("Type EVERYTHING YOU WANT to print on the screen.")
print("Type <quit> to quit.")
while 3 > 2:
    pr = input(settings.user + "> ")
    if pr == "quit":
        os.system('cls')
        print("WARNING : By exiting you'll quit from the Print Shell and PythonOS itself!")
        print("Type <yes> to continue, anything else to cancel...")
        a = input()
        if a == "yes":
            exit(0)
        else:
            pr
    else:
        print(pr)
