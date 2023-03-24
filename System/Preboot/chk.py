import importlib.util, os

class Check:
    def checkPackages(self, package='pip'):
        return bool(importlib.util.find_spec(package))

    def checkIntegrity(self, file='users.json'):
        return bool(os.path.exists(file))

    def checkDir(self, dir='../Boot'):
        return bool(os.path.isdir(dir))
