import time

class RecoveryMode:
    def __init__(self):
        print("PythonOS System couldn't start because one or more essential files are missing.")
        print("Now PythonRecovery will download required files from Github.")
        print("Make sure you have 'wget' pip pacakge installed.")
        input("If so, press Enter to continue. Else, quit from the program and install the package using 'pip install wget'")

    def downloadFiles(self, files='install.py'):
        pass