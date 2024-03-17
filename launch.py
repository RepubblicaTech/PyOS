from System.Preboot import pre, chk
from System.OS.Boot import boot
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
    time.sleep(1.5) 
    Install = install.Setup() # if user not present, boot innto installer

time.sleep(1)
prCheck = pre.PreBoot()

time.sleep(0.3)

files = ['System/users.json', 'System/OS/Shell/main.py']
foundFiles = 0

# Call the PKG_CHECK routine, then
# Check system integrity.
# Then boot if there are no problems

if (prCheck.checkPkgs() == True and prCheck.CheckOSIntegrity() == True):
    print("You're good to go! Booting into PyOS...")
    time.sleep(1)
    pass
else:
    print("Error PxC001: Something went wrong. Booting to recovery mode...")
    time.sleep(1)
    recovery = recover.RecoveryMode()

# Check if essential system files exist

for File in files:
    if chkFiles.checkIntegrity(file=File) == True:
        foundFiles += 1

if foundFiles == 2:
    print("System files found. Starting environment...")
    time.sleep(1)
    environment = boot.Boot()
else:
    print("Error BxC001: Some system files are missing. Booting into Recovery mode...")
    time.sleep(1)
    recovery = recover.RecoveryMode()
