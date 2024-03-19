from System.Preboot import pre, chk
from System.OS.Boot import boot
from System.OS.libs import errHandler
from System.Recovery import recover
from System import install
import time, os

print("Starting up...")
time.sleep(1)

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

if (prCheck.checkPkgs() == True and prCheck.CheckOSIntegrity() == True):
    print("You're good to go! Booting into PyOS...")
    pass
else:
    osIntegrityError = errHandler.Crash('preBoot', 'PxC001')
    recovery = recover.RecoveryMode()

# Check if essential system files exist
files = ['System/users.json', 'System/OS/Shell/main.py']
foundFiles = 0

for File in files:
    if chkFiles.checkIntegrity(file=File) == True:
        foundFiles += 1

if foundFiles == 2:
    print("System files found. Starting environment...")
    environment = boot.Boot()
else:
    missingFilesError = errHandler.Crash('preBoot', 'PBxC001')
    recovery = recover.RecoveryMode()
