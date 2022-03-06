import settings
import os
import colorama
print("Welcome to PythonOS v0.1 Update 1!")
print("Type <help> to see available commands.")

while 2 > 1:
    cwd = input(settings.user + "@pyos # ")

    if cwd == "update":
        import os

        os.system('pip install --upgrade pip')
        os.system('pip install --upgrade tqdm')
        os.system('pip install --upgrade requests')

    if cwd == "print":
        os.system('PrShell.py')
    if cwd == "help":
        print("5 available commands:")
        print("")
        print("help         See available commands")
        print("print        Works like <echo> in Windows, opens the Print Shell")
        print("update       Checks for updates, still doesn't update OS")
        print("about        Prints the system version")
        print("exit         Ends the PyOS process")
        print("")

    if cwd == "about":
        os.system('cls')
        print("PythonOS v0.1.1")
        print("")
        print("")
        print("Press Enter key to exit...")
        ee = input()
        if ee == "sinbad":
            os.system('cls')
            print("You have found the Sindbad Easter egg!")
            print("")
            colorama.init()
            sindbad = open("ascii-art.ans", 'r')
            print(sindbad.read())
            inpu

    if cwd == "exit":
        quit()
