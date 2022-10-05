from ensurepip import version
import os,platform,user,version

print("Welcome to " + version.name_full + version.about + "!")
print("Type <help> to see available commands.")

while True:
    cwd = input(user.user + "@pyos #> ")

    if cwd == "update":
        import os

        print("")
        os.system('pip install --upgrade pip')
        os.system('pip install --upgrade tqdm')
        print("")

    elif cwd == "print":
        os.system('cd Software && PrShell.py')
        os.system('cd ..')

    elif cwd == "help":
        print("7 available commands:")
        print("")
        print("help                 See available commands")
        print("print                Works like <echo> in Windows, opens the Print Shell.")
        print('echo                 As identical as to Windows and Unix: echo "some text here"')
        print("update               Checks for pip packages updates, still doesn't update OS.")
        print("about                Prints the system version.")
        print("exit                 Ends the PyOS process.")
        print("ver                  Same as <about>, but more detailed.")
        print("clear                Clears the shell input.")
        print("")

    elif cwd == "about":
        print("")
        print(version.name_full + version.about)
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
        print("")
        if ee == "sindbad":
            os.system('cls')
            print("You have unlocked the Sindbad Easter egg!")
            print("")
            sindbad = open("sinbad.txt", 'r')
            print(sindbad.read())
            input("Press Enter key to exit...")
            os.system('cls')

    elif cwd == "exit":
        quit()

    elif cwd == "ver":
        print("")
        print(version.name + version.ver)
        print("Kernel-" + version.krnl)
        print("")
        print("On " + platform.system() + " " + platform.release() + " build " + platform.version())
        print("")
        print("With Python " + platform.python_version())
        print("")
    
    elif cwd == "clear":
        os.system('cls')

    elif "echo" in cwd:
        ech = cwd.split("echo ")
        print(ech[1])

    else:
        print("Unknown command '" + cwd + "'. Type <help> to see available commands")