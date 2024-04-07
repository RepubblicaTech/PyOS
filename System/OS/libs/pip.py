import os, sys, subprocess, platform

system = sys.platform

def install(*packages):
    for package in packages:
        if system == "win32" or system == "darwin":
            os.system('python -m pip install ' + packages)
        elif system == "linux":
            try:
                subprocess.run(['pip'], check = True)
                print("\n\n")
            except subprocess.CalledProcessError:
                print("pip is not installed. Make sure to follow your distro's instructions to install it.")

def upgrade(*packages):
    for package in packages:
        if system == "win32" or system == "darwin":
            os.system(f'python -m pip install --upgrade {package}')
        elif system == "linux":
            try:
                subprocess.run(['pip'], check = True)
            except subprocess.CalledProcessError:
                print("pip is not installed. Make sure to follow your distro's instructions to install it.")
