class Argument:
    def __init__(self, name, options={}):
        self._name = name
        self._options = options

    def getName(self):
        return self._name
    
    def getOptions(self):
        return self._options