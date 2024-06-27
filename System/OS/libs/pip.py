import os, sys, subprocess, platform

system = sys.platform

def install(*packages):
    for package in packages:
        if system == "win32" or system == "darwin":
            os.system('python -m pip install ' + packages)
        elif system == "linux":
            print("Linux system detected.\nDue to the installation method changing from distro to distro, make sure to follow the instructions that suit more your OS.")
            exit(0)

def upgrade(*packages):
    for package in packages:
        if system == "win32" or system == "darwin":
            os.system(f'python -m pip install --upgrade {package}')
        elif system == "linux":
            print("Linux system detected.\nDue to the installation method changing from distro to distro,\nmake sure to follow the instructions that suit more your OS.")
            exit(0)
