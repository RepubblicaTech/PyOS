import os, time
import System.Preboot.chk as chk

class PreBoot:

    def checkPkgs(self, *packages) -> bool:
        self.found = 0
        self.required = 0
        self.missing = []

        for package in packages:
            self.required += 1
            self.activityOne = chk.Check()
            if self.activityOne.checkPackages(package) == True:
                self.found += 1
            else:
                self.missing.append(package)
            
        if self.found == self.required:
            return True
        else:
            return False

    def CheckOSIntegrity(self, dirs: list = ['Recovery', 'OS/Shell', 'OS/libs']) -> bool:
        
        self.required = 0
        self.foundDirs = 0
        for dir in dirs:
            self.required += 1
            if os.path.isdir(f'System/{dir}') == True:
                self.foundDirs += 1
                print(f"Found directory 'System/{dir}'.")
            else:
                print(f"Directory 'System/{dir}' not found.")

        if self.foundDirs == self.required:
            return True
        else:
            return False