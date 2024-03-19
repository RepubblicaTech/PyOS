import json, System.Preboot.chk as chk, System.OS.Shell.main as main

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

    def loginValidation(self, uname='root', passw='toor'):
        if passw == self.passwd and uname == self.username:
            systemDirCheck = chk.Check()
            if systemDirCheck.checkDir('System/OS/Shell') == False:
                print("Error LxL001: Shell environment not found. Make sure you have downloaded the full PythonOS package")
            
        else:
            print('Error LxL002: Either username or password are incorrect. Check users.json for credentials.')
            exit(0)

        session = main.Shell(self.uname)
