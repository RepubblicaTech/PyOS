import os

class RecoveryMode:
    def __init__(self, mode='recovery'):
        if (mode == "recovery"):
            print("PythonOS couldn't start because one or more essential files are missing.")
            print("Recovery mode is still under development.")
            input("Press Enter to exit...")
        elif (mode == "reset"):
            print("Deleting current PyOS Settings...")
            print(os.getcwd())
            exit(0)
        else:
            print("Error RxA001: Invalid argument for recovery mode. Quitting...")
            exit(0)
