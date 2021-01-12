from . import ls, helper, rm
active_commands = []

# comment the line to disable a specific command handler
def initilize(client):
    active_commands.append(ls.Command(client))
    active_commands.append(helper.Command(client))
    # active_commands.append(rm.Command(client)) # not ready