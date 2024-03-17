import os, time
import System.Preboot.chk as chk

# Step 1. Check for Python packages

class PreBoot:

    def checkPkgs(self):
        self.requiredPkgs = ['pip', 'tqdm', 'wget']
        self.found = 0

        for pkg in self.requiredPkgs:
            self.activityOne = chk.Check()
            self.activityOne.checkPackages(package=pkg)
            
            if self.activityOne.checkPackages() == True:
                self.found += 1
            
        if self.found < 3:
            print("Error PxC001: Cannot start PythonOS.\nThere are less or no packages installed than required (pip, tqdm, wget)")
        else:
            print("All required packages found.")
            return True
        

    def CheckOSIntegrity(self):
        self.requiredDirs = ['OS/Boot', 'Recovery']
        self.foundDirs = 0

        for dir in self.requiredDirs:
            if os.path.isdir(f'System/{dir}') == True:
                self.foundDirs += 1
                print(f"Found directory 'System/{dir}'.")
            
            else:
                print(f"Error PxC002: Directory '{dir}' is missing")

        if self.foundDirs == 2:
            print("All required directories found.")
        
        return True