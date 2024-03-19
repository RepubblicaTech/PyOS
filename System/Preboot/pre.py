import os, time
import System.Preboot.chk as chk

# Step 1. Check for Python packages

class PreBoot:

    def checkPkgs(self) -> bool:
        self.requiredPkgs = ['pip', 'tqdm', 'wget']
        self.found = 0

        for pkg in self.requiredPkgs:
            self.activityOne = chk.Check()
            self.activityOne.checkPackages(package=pkg)
            
            if self.activityOne.checkPackages() == True:
                self.found += 1
            
        if self.found < 3:
            return False
        else:
            print("All required packages found.")
            return True

    def CheckOSIntegrity(self) -> bool:
        self.requiredDirs = ['OS/Boot', 'Recovery']
        self.foundDirs = 0

        for dir in self.requiredDirs:
            if os.path.isdir(f'System/{dir}') == True:
                self.foundDirs += 1
                print(f"Found directory 'System/{dir}'.")

        if self.foundDirs == 2:
            print("All required directories found.")
            return True
        else:
            return False