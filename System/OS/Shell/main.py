import System.OS.Software.ver as ver
import System.OS.Software.PrShell as prsh
import json

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
            with open('System/OS/Shell/commands.json') as cmdJSON:
                self.jsonData = json.load(cmdJSON)
                print(self.jsonData['PyOS_Commands'])
        elif command == "ver":
            print(f"pyos-v{self.sysVersionVars.version_semantic}-k{self.sysVersionVars.kernel}")
            if ("b" in self.sysVersionVars.version_semantic) or ("a" in self.sysVersionVars.version_semantic):
                print(f"Codename \"{self.sysVersionVars.codename}\"")
        elif command == "prsh":
            PrSHSession = prsh.PrintShell(username)
        elif command == "":
            pass
        else:
            print(f"Error SxCH01: Invalid command <{command}>.")
