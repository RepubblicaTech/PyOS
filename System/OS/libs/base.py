import sys, os

# win32, linux, darwin
platform = sys.platform

def clearScreen():
    if (platform == "win32"):
        os.system('cls')
    elif (platform == "darwin" or platform == "linux"):
        os.system('clear')
