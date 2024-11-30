# error.py

class UslError(Exception):
    def __init__(self, message, line=None):
        super().__init__(message)
        self.line = line

    def __str__(self):
        if self.line:
            return f'{self.args[0]} at line {self.line}'
        else:
            return self.args[0]

class UslReturn(Exception):
    def __init__(self, value):
        self.value = value

class UslBreak(Exception):
    pass

class UslContinue(Exception):
    pass
