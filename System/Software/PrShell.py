import json, platform, os

print("Welcome to the Print Shell!")
print("Type <help> for commands.")

global username
username = ""

while True:
    pyos_env = json.load(open("../user.json"))

    for pyos in pyos_env['PyOS_Env']:
        username = pyos["Username"]

    pr = input(str(username) + "> ")
    if pr == "quit":
        if(platform.platform().__contains__("windows".lower())):
            os.system('cls')
        else:
            os.system('clear')
        exit(0)
    elif pr == "help":
        print("2 commands available:")
        print("")
        print("quit                         Quit from the Print Shell")
        print('"text"->"file.ext"               Writes text to a file')
        print("")
    elif "->" in pr:
        write = pr.split('->')

        f = open(write[1], 'w')
        f.write(write[0] + "\n")
        f.close()

        print("File saved in PyOS/System/Software/" + write[1] + '.')
    else:
        print(pr)