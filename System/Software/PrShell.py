import json, os

pyos_env = json.load(open("../users.json"))

for pyos in pyos_env['PyOS_Env']:
    
    global username
    global passwd
    username = pyos["Username"]
    passwd = pyos["Password"]

print("Welcome to the Print Shell!")
print("Type <help> for commands.")
while True:
    pr = input(str(username) + "> ")
    if pr == "quit":
        os.system('cls')
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