import System.OS.Software.ver as ver
import System.OS.Software.PrShell as prsh

class Shell:
    def __init__(self, username):
        self.sysVersionVars = ver.systemVersion('System/system.json')
        while True:
            self.cmd = input(f"{username}@vNext #> ")
            Shell.processInput(self, self.cmd, username)
    
    def processInput(self, command, username):
        if command == "exit":
            exit(0)
        elif command == "help":
            print("\nhelp                     Simply help.")
            print("exit                     Quits from the PythonOS environment.\n")
        elif command == "ver":
            print(f"pyos-v{self.sysVersionVars.version_semantic}_k{self.sysVersionVars.kernel}")
            if ("beta" in self.sysVersionVars.version_semantic) or ("alpha" in self.sysVersionVars.version_semantic):
                print(f"Codename \"{self.sysVersionVars.codename}\"")
        elif command == "prsh":
            PrSHSession = prsh.PrintShell(username)
        elif command == "":
            pass
        else:
            print(f"Error SxCH01: Invalid command <{command}>.")
