from System.Preboot import pre, chk
from System.OS.Boot import boot
from System.OS.libs import errHandler, base
from System.Recovery import recover
from System import install
import time, os

print("Starting up...")
time.sleep(1)

base.clearScreen()
print("REMEMBER: This is a pre-release version of PythonOS. It may not work as intended.\n")

# print(os.getcwd())

if(os.getcwd() == "C:\\Windows\\system32"):
    print("Due to some issues with double-clicking the launch.py,\nyou must start PythonOS from a terminal window in the PyOS directory.\nPress Enter to Exit.")
    input()
    exit(2)
else:
    pass

chkFiles = chk.Check()

if chkFiles.checkIntegrity('System/users.json'):
    pass                    # if user coniguration is present, boot into OS
else:
    print("Error PxJ001: users.json is missing, booting into installer...")
    Install = install.Setup() # if user not present, boot innto installer

prCheck = pre.PreBoot()


'''
Call the PKG_CHECK routine, then
Check system integrity.
Then boot if there are no problems

'''

if (prCheck.checkPkgs('pip', 'tqdm')):
    print("Required packages found.")
    pass
else:
    errHandler.Crash('preBoot', f'PxP001')
    print(prCheck.missing)
    exit(1)

if (prCheck.CheckOSIntegrity()):
    pass
else:
    errHandler.Crash('preBoot', 'PBxC001')
    recovery = recover.RecoveryMode()
    exit(1)

# Check if essential system files exist
files = ['System/users.json', 'System/OS/Shell/main.py']
foundFiles = 0

for File in files:
    if chkFiles.checkIntegrity(file=File) == True:
        foundFiles += 1

if foundFiles == 2:
    print("Required files found. Starting environment...")
    environment = boot.Boot()
else:
    errHandler.Crash('preBoot', 'PBxC001')
    recovery = recover.RecoveryMode()
    exit(1)
