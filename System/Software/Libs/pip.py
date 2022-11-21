import os, sys, subprocess

system = sys.platform

def install(package):
    if system == "win32" or system == "darwin":
        os.system('python -m pip install ' + package)
    elif system == "linux":
        try:
            subprocess.run(['pip'], check = True)
        except subprocess.CalledProcessError:
            os.system('sudo apt install -y python3-pip')
        
        os.system('pip3 install ' + package)

def upgrade(package):
    if system == "win32" or system == "darwin":
        os.system('python -m pip install --upgrade ' + package)
    elif system == "linux":
        try:
            subprocess.run(['pip'], check = True)
        except subprocess.CalledProcessError:
            os.system('sudo apt install python3-pip -y')
        
        os.system('pip3 install --upgrade ' + package)
