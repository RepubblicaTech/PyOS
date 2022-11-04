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

        if(platform.platform().__contains__("windows".lower())):
            print("")
            os.system('pip install --upgrade pip')
            os.system('pip install --upgrade tqdm')
            print("")
        else:
            print("")
            os.system('pip3 install --upgrade pip')
            os.system('pip3 install --upgrade tqdm')
            print("")

    elif cwd == "print":
        if(platform.platform().__contains__("windows".lower())):
            os.system('cls')
            os.system('cd Software && PrShell.py')
            os.system('cd ..')
        else:
            os.system('clear')
            os.system('cd Software && python3 PrShell.py')
            os.system('cd ..')
    elif cwd == "help":
        print("7 available commands:")
        print("")
        print("help                 See available commands")
        print("print                Opens the Print Shell. Has the ability to write txt to a file")
        print('echo SomeString      Identical as to Windows and Unix: echo "some text here"')
        print("read Yourfile.ext    Prints the content of a file.")
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
        if(platform.platform().__contains__("windows".lower())):
            os.system('cls')
        else:
            os.system('clear')

    elif "read" in cwd:
        print("")
        file = cwd.split("read ")
        f = open(file[1], 'r')
        print(f.read())

    elif "echo" in cwd:
        print(str(cwd).replace("echo ", ""))

    else:
        print("Unknown command '" + cwd + "'. Type <help> to see available commands")