import json
import System.Preboot.chk as chk, System.OS.Shell.main as main
from System.OS.libs import errHandler

class Login:
    def __init__(self, loginData='users.json'):

        self.username = ""
        self.passwd = ""
    
        self.pyos_env = json.load(open(loginData))

        for pyos in self.pyos_env['PyOS_Env']:
            self.username = pyos["Username"]
            self.passwd = pyos["Password"]

        self.uname = input("Enter your username: ")
        self.password = input(f"Enter {self.uname}'s password: ")
        Login.loginValidation(self, uname=self.uname, passw=self.password)

    def loginValidation(self, uname, passw):
        if passw == self.passwd and uname == self.username:
            systemDirCheck = chk.Check()
            if systemDirCheck.checkDir('System/OS/Shell') == False:
                missingShellError = errHandler.Crash('Login', 'LxL001')
        else:
            incorrectCredentialsError = errHandler.Crash('Login', 'LxL002')

        session = main.Shell(self.uname)
