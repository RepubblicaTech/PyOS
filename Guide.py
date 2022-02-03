import settings
import os
from pathlib import Path
from tqdm import tqdm
from time import sleep
import requests


def onea():
    os.system('cls')
    r = open("manual.py", "w")
    r.write("# 1a")
    r.close()
    print("Chapter 1a. The basics")
    print("")
    print("Welcome to the basics.")
    print("What you see down here is the information about the user and the directory")
    print("where you are working in.")
    print("")
    print('Try to type a name to replace with "user_name" (for example your username):')
    usr = input("user_name@directory # ")
    os.system('cls')
    print(usr.lower() + "@directory # ")
    print("Successful. Now, try to type 'cd home':")
    input(usr.lower() + "@directory # ")
    os.system('cls')
    print(usr.lower() + "@home # ")
    print("Well done!")
    input("Press Enter to go to the next chapter")
    os.system('cls')
    oneb()


def oneb():
    f = open("manual.py", "r")
    cron = f.read()
    if cron == "# 1a":
        f = open("manual.py", "w")
        f.write("# 1b")
        f.close()
    print("Chapter 1b. The Basics.")
    input()


print("Welcome to the PythonOS Start Guide!")
print("")
print("Press Enter to continue or type no to quit")
ask = input()
if ask == "no":
    os.system('cls')
    cwd = input(settings.user + "@pyos # ")

history = Path("manual.py")

if history.is_file():
    f = open("manual.py", "r")
    cron = f.read()
    if cron != "# 1a":
        print("We see that you have used the guide before.")
        print("Do you want to restore from the last visit [yes/no]?")
        a = input()
        if a == "yes":
            os.system('cls')
            for i in tqdm(range(100), desc='Searching for backup'):
                sleep(0.003)
            for i in tqdm(range(100), desc='Restoring from backup'):
                sleep(0.03)
            if cron == "# 1b":
                os.system('cls')
                oneb()
        elif a == "no":
            for i in tqdm(range(100), desc='Preparing for first run'):
                sleep(0.003)
                onea()
    elif cron == "":
        url = "http://www.python.org"
        try:
            request = requests.get(url, timeout=5)
            for i in tqdm(range(100), desc='Downloading required files'):
                sleep(0.04)
            for i in tqdm(range(100), desc='Installing dependencies'):
                sleep(0.02)
            f = open("manual.py", "w")
            f.write("# 1a")
            f.close()
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("Cannot Download Files. Connect to Internet")
    if cron == "# 1a":
        print("Do you want to continue with chapter 1b [yes/no]?")
        answer = input()
        if answer == "yes":
            oneb()
        elif answer == "no":
            onea()

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

