import json

class systemVersion:
    def __init__(self, versionData = 'System/system.json') -> None:
        self.jsonData = json.load(open(versionData))
        for data in self.jsonData['PyOS']:
            self.version = data["system_version"]
            self.version_semantic = data["system_semantic"]
            self.codename = data["system_codename"]
            self.kernel = data["kernel_version"]
