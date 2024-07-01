import os, shutil

class RecoveryMode:
    def __init__(self, mode='recovery'):
        if (mode == "recovery"):
            print("PythonOS couldn't start because one or more essential files are missing.")
            print("Recovery mode is still under development.\nYou can download")
            input("Press Enter to exit...")
        elif (mode == "reset"):
            input("WARNING: RESETTING PYOS WILL DELETE ALL SYSTEM SETTINGS AND FILES.\nIf you're sure to continue press enter.")

            # delete users.json
            print("Deleting System/users.json...")
            try:
                os.remove('System/users.json')
            except FileNotFoundError:
                # file has been already deleted
                pass

            # delete Users folder
            print("Deleting User folder...")
            try:
                os.rmdir('User')
            except OSError:
                # "Directory not empty" error
                shutil.rmtree('User')

            # Reset done
            input("Reset done succesufully! Press enter to quit and then open launch.py to start setup.")
            exit(0)
        else:
            print("Error RxA001: Invalid argument for recovery mode. Quitting...")
            exit(1)
