import settings
import os

print("Welcome to PythonOS v0.1.1")
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
        print("help                 See available commands")
        print("print                Works like <echo> in Windows, opens the Print Shell")
        print("update               Checks for updates, still doesn't update OS")
        print("about                Prints the system version")
        print("shutdown             Ends the PyOS process")
        print("<the hidden command> hint: POVERO GABBIANOOO!!!")
        print("")

    if cwd == "about":
        os.system('cls')
        print("PythonOS v0.1.1")
        print("")
        print("")
        print("Press Enter key to exit...")
        ee = input()
        if ee == "sindbad":
            os.system('cls')
            print("You have unlocked the Sindbad Easter egg!")
            print("")
            sindbad = open("ascii-art.txt", 'r')
            print(sindbad.read())
            input("Press Enter key to exit...")

    if cwd == "italy":
        os.system('cls')
        print("POVERO GABBIANOOO!!")
        print("HAI PERDUTO LA COMPAGNAAAA...")
        print("")
        sindbad = open("", 'r')
        print(sindbad.read())

    if cwd == "exit":
        quit()
