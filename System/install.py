from tqdm import tqdm
import time, json

class Setup:
    def __init__(self):
        self.obj = {}
        self.username = ""
        self.password = ""
        Setup.warning(self)
        print("Welcome to PythonOS version Next installer!")
        print("Please configure at least one user to make the environment work")
        Setup.configuration(self)
        Setup.dumpConfig(self)
        print("Install finished! You can quit the installer by pressing Enter then start launch.py")
        input()
        exit(0)
        
    def warning(self):
        print("WARNING: THIS IS A STRIPPED-DOWN VERSION OF PYTHONOS,\nUSE THIS FOR TESTING PURPOSES ONLY.")

    def configuration(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter a password (optional): ")
        input("If you are sure to continue, press Enter.")
        Setup.start(self)

    def start(self):
        for i in tqdm(range(100), desc='Setting up PythonOS environment'):
            time.sleep(0.03)

    def dumpConfig(self):
        self.obj["PyOS_Env"] = [{"Username": self.username, "Password": self.password}]
        self.pyos_json = open("System/users.json", "w")
        json.dump(self.obj, self.pyos_json, indent=2)

        
