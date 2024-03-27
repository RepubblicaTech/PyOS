import os, sys, subprocess

system = sys.platform

def install(*packages):
    for package in packages:
        if system == "win32" or system == "darwin":
            os.system('python -m pip install ' + packages)
        elif system == "linux":
            try:
                subprocess.run(['pip'], check = True)
            except subprocess.CalledProcessError:
                os.system('sudo apt install -y python3-pip')

            os.system(f'pip install {package}')

def upgrade(*packages):
    for package in packages:
        if system == "win32" or system == "darwin":
            os.system(f'python -m pip install --upgrade {package}')
        elif system == "linux":
            try:
                subprocess.run(['pip'], check = True)
            except subprocess.CalledProcessError:
                os.system('sudo apt install python3-pip -y')
            
            os.system(f'pip install --upgrade {package}')
