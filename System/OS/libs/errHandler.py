import json

phases = ['AlphaTestErrors', 'preBoot', 'Boot', 'Login', 'Shell']

class Crash:
    def __init__(self, Phase, errorCode) -> None:
        if (self.checkBootPhase(Phase) == 0):
            print("Cannot decode error code.")
        self.errorsJson = json.load(open('System/OS/libs/errors.json'))
        for error in self.errorsJson[Phase]:
            if (error['code'] == errorCode):
                self.returnError(error['code'], error['desc'])

    def returnError(self, errorCode, errorString) -> str:
        print(f'Error {errorCode}: {errorString}')
        return -1

    def checkBootPhase(self, Phase) -> int:
        i: int = 0
        for phase in phases:
            if (Phase == phase):
                i += 1
        if (i >= 1):
            return i
        else:
            return 0
