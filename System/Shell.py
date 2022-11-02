import os, platform, version, json

print("Welcome to " + version.name_full + version.about + "!")
print("Type <help> to see available commands.")

global username, passwd
username = ""
passwd = ""


while True:

    
    pyos_env = json.load(open("user.json"))

    for pyos in pyos_env['PyOS_Env']:
        username = pyos["Username"]
        passwd = pyos["Password"]
    
    cwd = input(username + "@pyos #> ")

    if cwd == "update":
        import os

        print("")
        os.system('pip install --upgrade pip')
        os.system('pip install --upgrade tqdm')
        print("")

    elif cwd == "print":
        os.system('cls')
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
        print("Setr0 (a schoolmate who helped me with JSON stuff)")
        print("Links:")
        print("Setr0's Github: https://github.com/Setr0")
        print("")

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

    elif "read" in cwd:
        print("")
        file = cwd.split("read ")
        f = open(file[1], 'r')
        print(f.read())

    elif "echo" in cwd:
        print(str(cwd).replace("echo ", ""))

    else:
        print("Unknown command '" + cwd + "'. Type <help> to see available commands")