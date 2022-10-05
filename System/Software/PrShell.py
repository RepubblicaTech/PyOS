import os

import user

print("Welcome to the Print Shell!")
print("Type <help> for commands.")
while True:
    pr = input(user.user + "> ")
    if pr == "quit":
        os.system('cls')
        exit(0)
    elif pr == "help":
        print("2 commands available:")
        print("")
        print("quit                         Quit from the Print Shell")
        print('"text"->"file.ext"               Writes text to a file')
    elif "->" in pr:
        write = pr.split('->')
        print(write)

        f = open(write[1], 'w')
        f.write(write[0] + "\n")
        f.close()
        f = open(write[1], 'r')
        print(f.read())
    else:
        print(pr)
