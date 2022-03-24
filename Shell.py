import settings
import os

print("Welcome to PythonOS v0.1.2 r2!")
print("Type <help> to see available commands.")

while 2 > 1:
    cwd = input(settings.user + "@pyos # ")

    if cwd == "update":
        import os

        os.system('pip install --upgrade pip')
        os.system('pip install --upgrade tqdm')
        os.system('pip install --upgrade requests')
    elif cwd == "print":
        os.system('PrShell.py')
    elif cwd == "help":
        print("6 available commands:")
        print("")
        print("help                 See available commands")
        print("print                Works like <echo> in Windows, opens the Print Shell")
        print("update               Checks for updates, still doesn't update OS")
        print("about                Prints the system version")
        print("exit                 Ends the PyOS process")
        print("<the hidden command> hint: POVERO GABBIANOOO!!!")
        print("")
    elif cwd == "about":
        os.system('cls')
        print("PythonOS v0.1.2")
        print("With Update 2")
        print("")
        print("Thanks to:")
        print("")
        print("The Python Team (For creating this easy language)")
        print("Life of Boris (with his videos, helped me to reach the programming adventure)")
        print("The Stack Overflow Community")
        print("YouTube")
        print("PyPl (for pip packages)")
        print("")
        print("Press Enter key to exit...")
        ee = input()
        if ee == "sindbad":
            os.system('cls')
            print("You have unlocked the Sindbad Easter egg!")
            print("")
            sindbad = open("sinbad.txt", 'r')
            print(sindbad.read())
            input("Press Enter key to exit...")
            os.system('cls')
    elif cwd == "italy":
        os.system('cls')
        print("POVERO GABBIANOOO!!")
        print("HAI PERDUTO LA COMPAGNAAAA...")
        print("")
        celeste = open("gianni.txt", 'r')
        print(celeste.read())
        input("Press Enter key to exit...")
        os.system('cls')
    elif cwd == "exit":
        quit()
    else:
        print("Unknown command '" + cwd + "'. Type <help> to see available commands")
