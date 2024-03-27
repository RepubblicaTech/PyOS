import os, time
import System.Preboot.chk as chk
import System.OS.login as login

def detectFiles(file='main.py'):
    return bool(os.path.isfile(str(file)))

class Boot:
    def __init__(self):
        self.login = login.Login(loginData='System/users.json')
