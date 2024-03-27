import time, json, os
from System.OS.libs import pip, base

try:
    from tqdm import tqdm
except ImportError:
    print("Package tqdm is not installed. Installing...")
    time.sleep(1)
    pip.install('tqdm')
    input("\nPackage tqdm has been installed successfully. Please quit the installer by pressing Enter and reopen launch.py.")
    exit(0)


class Setup:
    def __init__(self):
        self.obj = {}
        self.username = ""
        self.password = ""
        print("Welcome to the PythonOS installer!")
        print("Please configure at least one user to make the environment work")
        self.username = input("Enter your username: ")
        self.password = input("Enter a password (optional): ")
        input("If you are sure to continue, press Enter.")
        base.clearScreen()
        for i in tqdm(range(100), desc='Setting up PythonOS environment'):
            time.sleep(0.03)
        self.obj["PyOS_Env"] = [{"Username": self.username, "Password": self.password}]
        self.pyos_json = open("System/users.json", "w")
        json.dump(self.obj, self.pyos_json, indent=4)
        os.mkdir(f"User")
        os.mkdir(f"User/{self.username}")
        print("Install finished! You can quit the installer by pressing Enter then start launch.py")
        input()
        exit(0)

