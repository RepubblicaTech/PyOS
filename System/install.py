import time, json, System.OS.libs.pip as pip

try:
    from tqdm import tqdm
except ImportError:
    print("Package tqdm is not installed. Installing...")
    time.sleep(1)
    pip.install('tqdm')
    exit(1)


class Setup:
    def __init__(self):
        self.obj = {}
        self.username = ""
        self.password = ""
        print("WARNING: THIS IS A STRIPPED-DOWN VERSION OF PYTHONOS,\nUSE THIS FOR TESTING PURPOSES ONLY.")
        print("Welcome to PythonOS version Next installer!")
        print("Please configure at least one user to make the environment work")
        self.username = input("Enter your username: ")
        self.password = input("Enter a password (optional): ")
        input("If you are sure to continue, press Enter.")
        for i in tqdm(range(100), desc='Setting up PythonOS environment'):
            time.sleep(0.03)
        self.obj["PyOS_Env"] = [{"Username": self.username, "Password": self.password}]
        self.pyos_json = open("System/users.json", "w")
        json.dump(self.obj, self.pyos_json, indent=2)
        print("Install finished! You can quit the installer by pressing Enter then start launch.py")
        input()
        exit(0)

        
