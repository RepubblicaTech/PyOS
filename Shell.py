import settings
import os

while 2 > 1:
    cwd = input(settings.user + "@pyos # ")

    if cwd == "update":
        import os

        os.system('pip install --upgrade pip')
        os.system('pip install --upgrade tqdm')
        os.system('pip install --upgrade pathlib')
        os.system('pip install --upgrade requests')

    if cwd == "print":
        os.system('PrShell.py')

    if cwd == "help":
        print("4 available commands:")
        print("")
        print("help         See available commands")
        print("print        Works like <echo> in Windows, opens the Print Shell")
        print("update       Checks for updates, still doesn't update OS")
        print("about        prints the system version")

    if cwd == "about":
        os.system('cls')
        print("PyOS (or PythonOS) v0.1-update1")
        input("Press Enter key to exit...")
        os.system('cls')

    if cwd == "exit":
        quit()