class Shell:
    def __init__(self):
        while True:
            self.cmd = input("PyOS #> ")
            Shell.processInput(self, self.cmd)
    
    def processInput(self, command):
        if command == "exit":
            exit(0)
        if command == "help":
            print("\nhelp                     Simply help.")
            print("exit                     Quits from the PythonOS environment.\n")
        elif command == "":
            pass
        else:
            print(f"Error SxCH01: Invalid command <{command}>.")