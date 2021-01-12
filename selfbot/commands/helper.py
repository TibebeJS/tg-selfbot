from selfbot.types import UserbotCommand, Argument
from itertools import zip_longest
from asyncio import sleep

class Command(UserbotCommand):
    def __init__(self, instance):
        super().__init__(
            instance,
            command="help",
            sub_commands_required=False,
            arguments=[
                Argument(
                    "command",
                    options={
                        "help": "displays help information on that command.",
                        "nargs": "?",
                    },
                ),
            ],
            description="Provides help information for userbot commands. ",
        )

    async def handler(self, event, args):

        commands = map(lambda commandObj: f"`{commandObj.prefix}{commandObj.command}`", self.instance.active_commands)

        if args.command:
            try:
                await event.message.reply(list(filter(lambda command: command.command == args.command, self.instance.active_commands))[0].get_help())
            except IndexError:
                await event.message.reply(f"could not find the help for the command specified.")
        else:
            help_string = f"For more information on a specific command, type `.help <command-name>` or `<command> -h`\n\n"
            
            for command_group in zip_longest(*[iter(commands)]*2, fillvalue=' '):
                help_string += "             ".join(command_group) + "\n"

            await event.message.reply(
                help_string            
            )
            
        
        
