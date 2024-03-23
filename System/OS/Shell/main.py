from System.OS.Software import ver, PrShell as prsh
from System.OS.libs import base
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
                for command in self.jsonData['PyOS_Commands']:
                    print(f'{command['name']}\n  {command['desc']}\n')
        elif command == "ver":
            print(f"PythonOS version {self.sysVersionVars.version}", end='')
            if ("b" in self.sysVersionVars.version_semantic) or ("a" in self.sysVersionVars.version_semantic):
                print(f" Codename \"{self.sysVersionVars.codename}\"", end='')

            print(f"\npyos.v{self.sysVersionVars.version_semantic}_k{self.sysVersionVars.kernel}")

        elif command == "prsh":
            PrSHSession = prsh.PrintShell(username)
        elif command == "clear":
            base.clearScreen()
        elif command == "":
            pass
        else:
            print(f"Error SxCH01: Invalid command <{command}>.")
