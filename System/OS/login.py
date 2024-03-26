import json
import System.Preboot.chk as chk, System.OS.Shell.main as main
from System.OS.libs import errHandler, base

class Login:
    def __init__(self, loginData='users.json'):

        self.username = ""
        self.passwd = ""
        self.user = ""
        self.password = ""
    
        self.pyos_env = json.load(open(loginData))

        for pyos in self.pyos_env['PyOS_Env']:
            self.username = pyos["Username"]
            self.passwd = pyos["Password"]
        
        self.user = input("Enter your username: ")
        self.password = input(f"Enter {self.user}'s password: ")
        base.clearScreen()

        while (self.loginValidation(self.user, self.password) == False):
            errHandler.Crash('Login', 'LxL002')
            self.user = input("Enter your username: ")
            self.password = input(f"Enter {self.user}'s password: ")
            base.clearScreen()
        
        main.Shell(self.user)

    def loginValidation(self, uname, passw) -> bool:
        if passw == self.passwd and uname == self.username:
            systemDirCheck = chk.Check()
            if systemDirCheck.checkDir('System/OS/Shell') == False:
                errHandler.Crash('Login', 'LxL001')
                input()
                exit(1)
        else:
            return False
        
        return True
        # session = main.Shell(self.uname)
