from telethon import TelegramClient
from selfbot.types import SubCommand, Argument, CustomArgumentParser

from telethon.events import NewMessage
from io import StringIO
import shlex
import sys

class UserbotCommand:
    def __init__(
        self,
        instance,
        command,
        arguments=[],
        mutually_exclusive_arguments=[],
        sub_commands=[],
        description="",
        prefix=".",
        sub_commands_required=False,
        outgoing=True,
    ):
        self.instance = instance
        self.client = instance.client
        self.command = command
        self.arguments = arguments
        self.mutually_exclusive_arguments = mutually_exclusive_arguments
        self.sub_commands = sub_commands
        self.description = description
        self.prefix = prefix
        self.sub_commands_required = sub_commands_required

        self.outgoing = outgoing

        self.argparser = CustomArgumentParser(
            prog=f"{prefix}{command}", description=description
        )

        if len(sub_commands) > 0:
            subparsers = self.argparser.add_subparsers(
                dest="sub_command", required=sub_commands_required
            )

            for sub_command in sub_commands:
                sub_command_parser = subparsers.add_parser(
                    sub_command.getCommand(), description=sub_command.get_description()
                )
                for argument_group in sub_command.getMutuallyExclusiveArguments():
                    group = sub_command_parser.add_mutually_exclusive_group()
                    for argument in argument_group:
                        group.add_argument(argument.getName(), **argument.getOptions())

                for argument in sub_command.getArguments():
                    sub_command_parser.add_argument(
                        argument.getName(), **argument.getOptions()
                    )

        for argument_group in mutually_exclusive_arguments:
            group = self.argparser.add_mutually_exclusive_group()
            for argument in argument_group:
                group.add_argument(argument.getName(), **argument.getOptions())

        for argument in arguments:
            self.argparser.add_argument(argument.getName(), **argument.getOptions())

        self.client.add_event_handler(
            self.handler_wrapper,
            NewMessage(
                func=lambda x: x.message.message
                and x.message.message.startswith(f"{self.prefix}{self.command}"),
                outgoing=self.outgoing,
            ),
        )

    async def handler(self, event, args):
        await event.message.reply("The command handler is not implemented yet.")

    async def handler_wrapper(self, event):
        message = event.message

        sys.stdout = mystdout = StringIO()
        try:
            return await self.handler(
                event, args=self.argparser.parse_args(shlex.split(message.message)[1:]),
            )
        except SystemExit as error:
            await message.reply(mystdout.getvalue())
        except Exception as error:
            await message.reply(str(error))
        finally:
            sys.stdout = sys.__stdout__

    def get_help(self):
        return self.argparser.format_help()
