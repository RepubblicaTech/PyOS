import os
import platform
import settings
import keyboard

print("Welcome to PythonOS v0.1.3 Post-Reset Beta!")
print("Type <help> to see available commands.")

while 2 > 1:
    cwd = input(settings.user + "@pyos # ")

    if cwd == "update":
        import os

        print("")
        os.system('pip install --upgrade pip')
        os.system('pip install --upgrade tqdm')
        os.system('pip install --upgrade requests')
        os.system('pip install --upgrade pywin32')
        os.system('pip install keyboard')
        print("")

    elif cwd == "print":
        os.system('PrShell.py')

    elif cwd == "help":
        print("7 available commands:")
        print("")
        print("help                 See available commands")
        print("print                Works like <echo> in Windows, opens the Print Shell")
        print("update               Checks for updates, still doesn't update OS")
        print("about                Prints the system version")
        print("exit                 Ends the PyOS process")
        print("<the hidden command> hint: spaghetti country")
        print("ver                  Same as <about>, but more detailed.")
        print("")

    elif cwd == "about":
        os.system('cls')
        print("PythonOS v0.1.3 Post-Reset Beta 1")
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
        os.system('cls')
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

    elif cwd == "ver":
        print("")
        print("PyOS v0.1.3-reset.1")
        print("Kernel version 0.2-beta.3")
        print("")
        print("On " + platform.system() + " " + platform.release() + " build " + platform.version())
        print("")
        print("With Python " + platform.python_version())
        print("")

    elif cwd == "features":
        print("Press f to see new features in this build, or press r to see all OS features:")
        if keyboard.read_key() == "f":
            os.system('cls')
            print("New features:")
            f = open("Features!.txt", "r")
            print(f.read())
            print("")

    else:
        print("Unknown command '" + cwd + "'. Type <help> to see available commands")
