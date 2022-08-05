import os

from System import settings

print("Welcome to the Print Shell!")
print("Type EVERYTHING YOU WANT to print on the screen.")
print("Type <quit> to quit.")
while 3 > 2:
    pr = input(settings.user + "> ")
    if pr == "quit":
        os.system('cls')
        exit(0)
    else:
        print(pr)
