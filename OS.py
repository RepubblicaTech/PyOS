import settings
import os
from pathlib import Path
from tqdm import tqdm
from time import sleep
import requests

print("Welcome to PythonOS!")
print("PythonOS login:")
user_name = input()

if user_name == settings.user:
    print("Enter password:")
    password = input()
    if password == settings.passwd:
        print("Welcome!")
        cwd = input(settings.user + "@pyos # ")
    else:
        print("Incorrect password. Close this windows and reopen OS.py")
        input()
else:
    print("Incorrect username. Quit and reopen OS.py")
    input("Press Enter key to quit...")

if cwd == "start":
    os.system('cls')
    print("Welcome to the PythonOS Start Guide!")
    print("Press Enter to continue or type no to quit")
    ask = input()
    if ask == "no":
        os.system('cls')
        cwd = input(settings.user + "@pyos # ")

history = Path("manual.py")

if history.is_file():
    f = open("manual.py", "r")
    cron = f.read()
    nothing = "chron = " + '""'
    if cron != "#":
        print("We see that you have used the guide before.")
        print("Do you want to restore from the last visit [yes/no]?")
        a = input()
        if a == "yes":
            for i in tqdm(range(100), desc='Searching for backup'):
                sleep(0.003)
            for i in tqdm(range(100), desc='Restoring from backup'):
                sleep(0.03)
            if cron == "# 1b":
                print("You are on Chapter 1b.")
        elif a == "no":
            for i in tqdm(range(100), desc='Preparing for first run'):
                sleep(0.003)
    elif cron == "":
        url = "http://www.python.org"
        try:
            request = requests.get(url, timeout=5)
            for i in tqdm(range(100), desc='Downloading required files'):
                sleep(0.04)
            for i in tqdm(range(100), desc='Installing dependencies'):
                sleep(0.02)
            f = open("manual.py", "w")
            f.write("chron = " + '"1"')
            f.close()
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("Cannot Download Files. Connect to Internet")
else:
    for i in tqdm(range(100), desc='Preparing for first run'):
        sleep(0.003)
    url = "http://www.python.org"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        for i in tqdm(range(100), desc='Downloading required files'):
            sleep(0.03)
        for i in tqdm(range(100), desc='Installing dependencies'):
            sleep(0.03)
        f = open("manual.py", "x")
        f.close()
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("Cannot Download Files. Connect to Internet")
