import json

phases = ['AlphaTestErrors', 'preBoot', 'Boot', 'Login', 'Shell']

class Crash:
    def __init__(self, Phase, errorCode) -> None:
        if (self.checkBootPhase(Phase) == 0):
            self.halt()
        self.errorsJson = json.load(open('System/OS/libs/errors.json'))
        for error in self.errorsJson[Phase]:
            if (error['code'] == errorCode):
                print(f'Error {error['code']}: {error['desc']}')


    def checkBootPhase(self, Phase) -> int:
        i: int = 0
        for phase in phases:
            if (Phase == phase):
                i += 1
        if (i >= 1):
            return i
        else:
            return (not i)  
