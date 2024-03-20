import os, time
import System.Preboot.chk as chk

# Step 1. Check for Python packages

class PreBoot:

    def checkPkgs(self, packages: list = ['pip', 'tqdm']) -> bool:
        self.found = 0
        self.required = 0
        self.missing = []

        for pack in packages:
            self.required += 1

        for pkg in packages:
            self.activityOne = chk.Check()
            if self.activityOne.checkPackages(pkg) == True:
                self.found += 1
            else:
                self.missing.append(pkg)
            
        if self.found != self.required:
            return False
        else:
            return True

    def CheckOSIntegrity(self, dirs: list = ['OS/Boot', 'Recovery']) -> bool:
        self.foundDirs = 0

        for dir in dirs:
            if os.path.isdir(f'System/{dir}') == True:
                self.foundDirs += 1
                print(f"Found directory 'System/{dir}'.")

        if self.foundDirs == 2:
            return True
        else:
            return False