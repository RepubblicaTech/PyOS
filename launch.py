from System.Preboot import pre, chk
from System.OS.Boot import boot
from System import install
import time, os

print("Starting up...")
time.sleep(1)

if os.path.isfile('System/users.json'):
    pass                    # if user coniguration is present, boot into OS
else:
    print("Error PxJ001: users.json is missing, booting into installer...")
    time.sleep(1.5) 
    Install = install.Setup()

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
    print("Error PxC001: Something went wrong. Please check all the errors to solve them.")
    exit(0)

# Check if essential system files exist

for File in files:
    chkFiles = chk.Check()
    if chkFiles.checkIntegrity(file=File) == True:
        foundFiles += 1

if foundFiles == 2:
    print("System files found. Starting environment...")
    time.sleep(1)
    environment = boot.Boot()
else:
    print("Error BxC001: Some system files are missing. Booting into Recovery mode...")
    exit(0)
