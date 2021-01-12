class SubCommand:
    def __init__(self, command, description="", arguments=[], mutually_exclusive_arguments=[]):
        self._command = command
        self._description = description
        self._arguments = arguments
        self._mutually_exclusive_arguments = mutually_exclusive_arguments
    def getCommand(self):
        return self._command
    def get_description(self):
        return self._description
    def getArguments(self):
        return self._arguments
    def getMutuallyExclusiveArguments(self):
        return self._mutually_exclusive_arguments