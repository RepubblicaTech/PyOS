import json, os

class PrintShell:
    def __init__(self, username: str) -> None:
        print("Welcome to the Print Shell!")
        print("Type <help> for commands.")
        self.name = username
        while True:

            pr = input(self.name + "> ")
            if pr == "quit":
                os.system('cls')
                exit(0)
            elif pr == "help":
                print("2 commands available:")
                print("")
                print("quit                         Quit from the Print Shell")
                print('text->file.ext               Writes text to a file')
                print("")
            elif "->" in pr:
                write = pr.split('->')

                f = open(write[1], 'w')
                f.write(write[0] + "\n")
                f.close()

                print(f"File saved in PyOS:0/System/Software/{write[1]}.")
            else:
                print(pr)
