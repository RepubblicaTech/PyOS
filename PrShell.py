import settings
import os

print("Welcome to the Print Shell!")
print("Type EVERYTHING YOU WANT to print on the screen.")
print("Type <exit> to quit.")
while 3 > 2:
    pr = input(settings.user + "> ")
    if pr == "exit":
        os.system('cls')
        os.system('Shell.py')
    else:
        print(pr)
